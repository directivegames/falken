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

class CallOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCallOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CallOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def CallOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # CallOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CallOptions
    def Subgraph(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def CallOptionsStart(builder): builder.StartObject(1)
def CallOptionsAddSubgraph(builder, subgraph): builder.PrependUint32Slot(0, subgraph, 0)
def CallOptionsEnd(builder): return builder.EndObject()


class CallOptionsT(object):

    # CallOptionsT
    def __init__(self):
        self.subgraph = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        callOptions = CallOptions()
        callOptions.Init(buf, pos)
        return cls.InitFromObj(callOptions)

    @classmethod
    def InitFromObj(cls, callOptions):
        x = CallOptionsT()
        x._UnPack(callOptions)
        return x

    # CallOptionsT
    def _UnPack(self, callOptions):
        if callOptions is None:
            return
        self.subgraph = callOptions.Subgraph()

    # CallOptionsT
    def Pack(self, builder):
        CallOptionsStart(builder)
        CallOptionsAddSubgraph(builder, self.subgraph)
        callOptions = CallOptionsEnd(builder)
        return callOptions
