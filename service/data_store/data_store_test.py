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

"""Tests for DataStore."""

import re

from absl.testing import absltest
from data_store import data_store

import common.generate_protos  # pylint: disable=g-bad-import-order,unused-import

import data_store_pb2


class FakeFileSystem(object):
  """In-memory implementation of the FileSystem class."""

  def __init__(self):
    self._path_to_proto = {}
    # Simulate the passing of time with a counter.
    self._current_time = 0

  def read_proto(self, pattern, unused_data_type):
    """Finds matching file path, and reads its binary proto data.

    Args:
      pattern: The path pattern of the file where the proto is stored, including
        a single * to allow for unknown parts of the name to be filled in.
        No more than one file is allowed to match with the pattern path.
      unused_data_type: The class of the proto to read.
    Returns:
      The proto that was read from storage.
    """
    assert pattern.count('*') == 1
    paths = self.glob(pattern)
    assert len(paths) == 1
    return self._path_to_proto[paths[0]]

  def write_proto(self, pattern, data):
    """Writes proto data into the given file.

    Args:
      pattern: The path of the file where the proto is stored, with a * that
        will be replaced by the timestamp.
      data: A proto to store in that location.
    """
    assert pattern.count('*') == 1
    path = pattern.replace('*', str(self._current_time))
    self._path_to_proto[path] = data
    self._current_time += 1

  def glob(self, pattern):
    """Encapsulates glob.glob.

    Args:
      pattern: Pattern to search for.
    Returns:
      List of path strings found.
    """
    # The fake file system doesn't support recursive globs.
    assert '**' not in pattern
    pattern = pattern.replace('*', '[^/]*')
    return [path for path in sorted(self._path_to_proto)
            if re.match(pattern, path)]


class DataStoreTest(absltest.TestCase):

  def setUp(self):
    """Create a datastore object that uses a temporary directory."""
    super().setUp()
    self._data_store = data_store.DataStore(FakeFileSystem())

  def tearDown(self):
    """Clean up the temporary directory and datastore."""
    super().tearDown()
    self._data_store = None

  def test_read_write_project(self):
    self._data_store.write_project(data_store_pb2.Project(project_id='p1'))
    self.assertEqual('p1', self._data_store.read_project('p1').project_id)

  def test_read_write_brain(self):
    self._data_store.write_brain(
        data_store_pb2.Brain(project_id='p1', brain_id='b1'))
    self.assertEqual('b1', self._data_store.read_brain('p1', 'b1').brain_id)

  def test_read_write_snapshot(self):
    self._data_store.write_snapshot(data_store_pb2.Snapshot(
        project_id='p1', brain_id='b1', snapshot_id='s1'))
    self.assertEqual(
        's1', self._data_store.read_snapshot('p1', 'b1', 's1').snapshot_id)

  def test_read_write_session(self):
    self._data_store.write_session(data_store_pb2.Session(
        project_id='p1', brain_id='b1', session_id='s1'))
    self.assertEqual(
        's1', self._data_store.read_session('p1', 'b1', 's1').session_id)

  def test_read_write_episode_chunk(self):
    self._data_store.write_episode_chunk(data_store_pb2.EpisodeChunk(
        project_id='p1', brain_id='b1', session_id='s1', episode_id='e1',
        chunk_id=3))
    self.assertEqual(3, self._data_store.read_episode_chunk(
        'p1', 'b1', 's1', 'e1', 3).chunk_id)

  def test_read_write_online_evaluation(self):
    self._data_store.write_online_evaluation(
        data_store_pb2.OnlineEvaluation(
            project_id='p1', brain_id='b1', session_id='s1', episode_id='e1'))
    self.assertEqual(
        'e1',
        self._data_store.read_online_evaluation('p1', 'b1', 's1',
                                                'e1').episode_id)

  def test_read_write_assignment(self):
    self._data_store.write_assignment(
        data_store_pb2.Assignment(
            project_id='p1', brain_id='b1', session_id='s1',
            assignment_id='a1'))
    self.assertEqual(
        'a1',
        self._data_store.read_assignment('p1', 'b1', 's1', 'a1').assignment_id)

  def test_read_write_model(self):
    self._data_store.write_model(data_store_pb2.Model(
        project_id='p1', brain_id='b1', session_id='s1', model_id='m1'))
    self.assertEqual(
        'm1', self._data_store.read_model('p1', 'b1', 's1', 'm1').model_id)

  def test_read_write_serialized_model(self):
    self._data_store.write_serialized_model(data_store_pb2.SerializedModel(
        project_id='p1', brain_id='b1', session_id='s1', model_id='m1'))
    self.assertEqual('m1', self._data_store.read_serialized_model(
        'p1', 'b1', 's1', 'm1').model_id)

  def test_read_write_offline_evaluation(self):
    self._data_store.write_offline_evaluation(
        data_store_pb2.OfflineEvaluation(
            project_id='p1',
            brain_id='b1',
            session_id='s1',
            model_id='m1',
            evaluation_set_id=2))
    self.assertEqual(
        2,
        self._data_store.read_offline_evaluation('p1', 'b1', 's1', 'm1',
                                                 2).evaluation_set_id)

  def test_get_project_path(self):
    self.assertEqual('projects/p1', self._data_store._get_project_path('p1'))

  def test_get_brain_path(self):
    self.assertEqual('projects/p1/brains/b1',
                     self._data_store._get_brain_path('p1', 'b1'))

  def test_get_snapshot_path(self):
    self.assertEqual('projects/p1/brains/b1/snapshots/s1',
                     self._data_store._get_snapshot_path('p1', 'b1', 's1'))

  def test_get_session_path(self):
    self.assertEqual('projects/p1/brains/b1/sessions/s1',
                     self._data_store._get_session_path('p1', 'b1', 's1'))

  def test_get_episode_path(self):
    self.assertEqual('projects/p1/brains/b1/sessions/s1/episodes/e1',
                     self._data_store._get_episode_path('p1', 'b1', 's1', 'e1'))

  def test_get_chunk_path(self):
    self.assertEqual(
        'projects/p1/brains/b1/sessions/s1/episodes/e1/chunks/c1',
        self._data_store._get_chunk_path('p1', 'b1', 's1', 'e1', 'c1'))

  def test_get_assignment_path(self):
    self.assertSequenceStartsWith(
        'projects/p1/brains/b1/sessions/s1/assignments/',
        self._data_store._get_assignment_path('p1', 'b1', 's1', 'a1'))

  def test_get_model_path(self):
    self.assertEqual('projects/p1/brains/b1/sessions/s1/models/m1',
                     self._data_store._get_model_path('p1', 'b1', 's1', 'm1'))

  def test_get_offline_evaluation_path(self):
    self.assertEqual(
        'projects/p1/brains/b1/sessions/s1/models/m1/offline_evaluations/o1',
        self._data_store._get_offline_evaluation_path(
            'p1', 'b1', 's1', 'm1', 'o1'))


if __name__ == '__main__':
  absltest.main()
