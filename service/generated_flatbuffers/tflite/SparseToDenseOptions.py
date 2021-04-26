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
#
# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SparseToDenseOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSparseToDenseOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SparseToDenseOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def SparseToDenseOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SparseToDenseOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SparseToDenseOptions
    def ValidateIndices(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def SparseToDenseOptionsStart(builder): builder.StartObject(1)
def SparseToDenseOptionsAddValidateIndices(builder, validateIndices): builder.PrependBoolSlot(0, validateIndices, 0)
def SparseToDenseOptionsEnd(builder): return builder.EndObject()


class SparseToDenseOptionsT(object):

    # SparseToDenseOptionsT
    def __init__(self):
        self.validateIndices = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        sparseToDenseOptions = SparseToDenseOptions()
        sparseToDenseOptions.Init(buf, pos)
        return cls.InitFromObj(sparseToDenseOptions)

    @classmethod
    def InitFromObj(cls, sparseToDenseOptions):
        x = SparseToDenseOptionsT()
        x._UnPack(sparseToDenseOptions)
        return x

    # SparseToDenseOptionsT
    def _UnPack(self, sparseToDenseOptions):
        if sparseToDenseOptions is None:
            return
        self.validateIndices = sparseToDenseOptions.ValidateIndices()

    # SparseToDenseOptionsT
    def Pack(self, builder):
        SparseToDenseOptionsStart(builder)
        SparseToDenseOptionsAddValidateIndices(builder, self.validateIndices)
        sparseToDenseOptions = SparseToDenseOptionsEnd(builder)
        return sparseToDenseOptions
