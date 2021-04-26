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

class GatherOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGatherOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GatherOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GatherOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # GatherOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GatherOptions
    def Axis(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GatherOptions
    def BatchDims(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def GatherOptionsStart(builder): builder.StartObject(2)
def GatherOptionsAddAxis(builder, axis): builder.PrependInt32Slot(0, axis, 0)
def GatherOptionsAddBatchDims(builder, batchDims): builder.PrependInt32Slot(1, batchDims, 0)
def GatherOptionsEnd(builder): return builder.EndObject()


class GatherOptionsT(object):

    # GatherOptionsT
    def __init__(self):
        self.axis = 0  # type: int
        self.batchDims = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        gatherOptions = GatherOptions()
        gatherOptions.Init(buf, pos)
        return cls.InitFromObj(gatherOptions)

    @classmethod
    def InitFromObj(cls, gatherOptions):
        x = GatherOptionsT()
        x._UnPack(gatherOptions)
        return x

    # GatherOptionsT
    def _UnPack(self, gatherOptions):
        if gatherOptions is None:
            return
        self.axis = gatherOptions.Axis()
        self.batchDims = gatherOptions.BatchDims()

    # GatherOptionsT
    def Pack(self, builder):
        GatherOptionsStart(builder)
        GatherOptionsAddAxis(builder, self.axis)
        GatherOptionsAddBatchDims(builder, self.batchDims)
        gatherOptions = GatherOptionsEnd(builder)
        return gatherOptions
