# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Tests for model_selection_record."""

from absl.testing import absltest

from api import model_selection_record


class ModelScoresTest(absltest.TestCase):

  def test_model_scores_sorted_by_score(self):
    scores = model_selection_record.ModelScores()
    scores.add_score('model_id_0', 20.0)
    scores.add_score('model_id_1', 0.2)
    scores.add_score('model_id_2', -0.2)
    # Worse than the worst, so does not get added.
    scores.add_score('model_id_2', 30.0)
    self.assertEqual(scores.model_scores,
                     [model_selection_record.ModelScore('model_id_2', -0.2),
                      model_selection_record.ModelScore('model_id_1', 0.2),
                      model_selection_record.ModelScore('model_id_0', 20.0)])

  def test_model_ids(self):
    scores = model_selection_record.ModelScores()
    scores.add_score('model_id_0', 20.0)
    scores.add_score('model_id_1', 0.2)
    scores.add_score('model_id_2', -0.2)
    scores.add_score('model_id_2', 0.9)
    self.assertEqual(scores.model_ids,
                     set(['model_id_0', 'model_id_1', 'model_id_2']))


class OfflineEvaluationByAssignmentAndEvalIdTest(absltest.TestCase):

  def test_scores_by_offline_evaluation_id(self):
    scores = model_selection_record.OfflineEvaluationByAssignmentAndEvalId(
        model_selection_record.ModelScores)
    scores[model_selection_record.AssignmentEvalId('a0', 0)].add_score(
        'model_id_0', 0.8)
    scores[model_selection_record.AssignmentEvalId('a0', 1)].add_score(
        'model_id_1', -76.0)
    scores[model_selection_record.AssignmentEvalId('a2', 2)].add_score(
        'model_id_2', -0.2)
    scores[model_selection_record.AssignmentEvalId('a2', 1)].add_score(
        'model_id_3', -0.2)
    scores[model_selection_record.AssignmentEvalId('a2', 1)].add_score(
        'model_id_3', -30)
    self.assertEqual(
        scores.scores_by_offline_evaluation_id('a0'),
        [(1, model_selection_record.ModelScore(
            model_id='model_id_1', score=-76.0)),
         (0, model_selection_record.ModelScore(
             model_id='model_id_0', score=0.8))])
    self.assertEqual(
        scores.scores_by_offline_evaluation_id('a2'),
        [(2, model_selection_record.ModelScore(
            model_id='model_id_2', score=-0.2)),
         (1, model_selection_record.ModelScore(
             model_id='model_id_3', score=-30)),
         (1, model_selection_record.ModelScore(
             model_id='model_id_3', score=-0.2))])

  def test_model_ids_for_assignment_id(self):
    scores = model_selection_record.OfflineEvaluationByAssignmentAndEvalId(
        model_selection_record.ModelScores)
    scores[model_selection_record.AssignmentEvalId('a0', 0)].add_score(
        'model_id_0', 0.8)
    scores[model_selection_record.AssignmentEvalId('a0', 0)].add_score(
        'model_id_1', -76.0)
    scores[model_selection_record.AssignmentEvalId('a2', 1)].add_score(
        'model_id_2', -22.0)
    scores[model_selection_record.AssignmentEvalId('a2', 1)].add_score(
        'model_id_3', -0.2)
    self.assertEqual(
        scores.model_ids_for_assignment_id('a0'),
        set(['model_id_0', 'model_id_1']))

  def test_assignment_ids(self):
    scores = model_selection_record.OfflineEvaluationByAssignmentAndEvalId(
        model_selection_record.ModelScores)
    scores[model_selection_record.AssignmentEvalId('a0', 0)].add_score(
        'model_id_0', 0.8)
    scores[model_selection_record.AssignmentEvalId('a0', 0)].add_score(
        'model_id_1', -76.0)
    scores[model_selection_record.AssignmentEvalId('a2', 1)].add_score(
        'model_id_2', -22.0)
    scores[model_selection_record.AssignmentEvalId('a2', 1)].add_score(
        'model_id_3', -0.2)
    self.assertEqual(scores.assignment_ids, set(['a0', 'a2']))


if __name__ == '__main__':
  absltest.main()
