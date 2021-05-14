// Copyright 2021 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "falken_player_dynamic.h"
#include <SDL.h>
#include <assert.h>

#include "ship.h"

namespace hello_falken {

static const char *kAPIKey = nullptr;    // Set your API key here
static const char *kProjectId = nullptr; // Set your Project key here

bool FalkenPlayer::Init(const char *brain_id, const char *snapshot_id) {
  falken::ObservationsBase observations;

  // Dynamically bind goal entity.
  falken::EntityBase goal(observations, "goal");

  falken::ActionsBase actions;
  // Dynamically bind the steering & throttle attributes to the actions.
  falken::AttributeBase steering(actions, "steering",
                                 falken::kAxesModeDeltaPitchYaw,
                                 falken::kControlledEntityPlayer,
                                 falken::kControlFrameWorld);
  falken::AttributeBase throttle(actions, "throttle", -1.0f, 1.0f);

  falken::BrainSpecBase brain_spec_base(&observations, &actions);

  assert(service_ == nullptr);
  service_ = falken::Service::Connect(kProjectId, kAPIKey);
  if (service_ != nullptr) {
    SDL_Log("Connected to Falken!\n");
    static const char *kBrainName = "DynamicBinding_Brain";
    if (!brain_id) {
      brain_ = service_->CreateBrain(kBrainName, brain_spec_base);
    } else {
      brain_ = service_->GetBrain(brain_id, snapshot_id);
    }
    if (brain_ != nullptr) {
      SDL_Log("Created brain: %s\n", brain_->id());
      session_ = brain_->StartSession(falken::Session::kTypeInteractiveTraining,
                                      kMaxSteps);
      if (session_ != nullptr) {
        SDL_Log("Started session: %s\n", session_->id());
      }
    }
  }
  return session_ != nullptr;
}

void FalkenPlayer::StartEvaluationSession(bool forced_evaluation) {
  if (forced_evaluation) {
    SDL_Log("User triggered evaluation mode.\n");
  } else {
    SDL_Log("Training complete.\n");
  }
  StopSession();
  session_ = brain_->StartSession(falken::Session::kTypeEvaluation, kMaxSteps);
  if (session_ != nullptr) {
    SDL_Log("Started eval session: %s\n", session_->id());
  }
  episode_ = session_->StartEpisode();
}

void FalkenPlayer::StartInferenceSession() {
  // Because the episode was started at Reset, Step the episode before stopping
  // with an empty episode.
  episode_->Step(0.f);
  StopSession();

  session_ = brain_->StartSession(falken::Session::kTypeInference, kMaxSteps);
  if (session_ == nullptr) {
    SDL_Log("Could not start inference session.\n");
    return;
  }

  SDL_Log("Started inference session: %s\n", session_->id());
  episode_ = session_->StartEpisode();
}

bool FalkenPlayer::Update(Ship &ship, Goal &goal, bool human_control,
                          bool force_evaluation) {

  if (episode_ != nullptr) {
    // Change session type when training is complete or the player requests
    // an evaluation session.
    bool training_complete =
        session_->training_state() == falken::Session::kTrainingStateComplete;
    switch (session_->type()) {
    case falken::Session::kTypeInteractiveTraining:
      if (training_complete || force_evaluation) {
        StartEvaluationSession(force_evaluation);
      }
      break;
    case falken::Session::kTypeEvaluation:
      if (training_complete)
        StartInferenceSession();
      break;
    default:
      break;
    }
    auto &brain_spec = brain_->brain_spec_base();

    // Dynamically retrieve the angle attribute from the observations and set
    // the value.
    brain_spec.observations_base().position.set_value(
        AsXZPosition(ship.position));
    brain_spec.observations_base().rotation.set_value(
        HFAngleToQuaternion(ship.rotation));
    brain_spec.observations_base().entity("goal")->position.set_value(
        AsXZPosition(goal.position));
    brain_spec.observations_base().entity("goal")->rotation.set_value(
        HFAngleToQuaternion(0));

    if (human_control) {
      brain_spec.actions_base().set_source(
          falken::ActionsBase::kSourceHumanDemonstration);
      // Dynamically retrieve the steering & throttle attributes from the
      // actions and set the values.
      brain_spec.actions_base().attribute("steering")->set_joystick_x_axis(
        ship.GetSteering());
      brain_spec.actions_base().attribute("steering")->set_joystick_y_axis(0);
      brain_spec.actions_base().attribute("throttle")->set_number(
        ship.GetThrottle());
    } else {
      brain_spec.actions_base().set_source(falken::ActionsBase::kSourceNone);
    }
    episode_->Step(0.f);
    if (episode_->completed()) {
      episode_ = nullptr;
      return true;
    } else if (!human_control) {
      ship.SetControls(
        brain_spec.actions_base().attribute("steering")->joystick_x_axis(),
        brain_spec.actions_base().attribute("throttle")->number());
    }
  }
  return false;
}

void FalkenPlayer::StopSession() {
  if (episode_ != nullptr) {
    episode_->Complete(falken::Episode::kCompletionStateAborted);
    episode_ = nullptr;
  }
  if (session_ != nullptr) {
    auto snapshot_id = session_->Stop();
    SDL_Log("Stopped session with snapshot ID %s\n", snapshot_id.c_str());
    session_ = nullptr;
  }
}

void FalkenPlayer::Reset(bool success) {
  if (episode_ != nullptr && !episode_->completed()) {
    episode_->Complete(success ? falken::Episode::kCompletionStateSuccess
                               : falken::Episode::kCompletionStateFailure);
  }
  if (session_ != nullptr) {
    episode_ = session_->StartEpisode();
  }
}

void FalkenPlayer::Shutdown() {
  StopSession();

  // This will automatically delete the underlying objects
  SDL_Log("Shutting down brain: %s.\n", brain_->id());
  brain_ = nullptr;
  service_ = nullptr;
}
} // namespace hello_falken