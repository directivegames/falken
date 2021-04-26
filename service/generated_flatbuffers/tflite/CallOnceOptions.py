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

class CallOnceOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCallOnceOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CallOnceOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def CallOnceOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # CallOnceOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CallOnceOptions
    def InitSubgraphIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def CallOnceOptionsStart(builder): builder.StartObject(1)
def CallOnceOptionsAddInitSubgraphIndex(builder, initSubgraphIndex): builder.PrependInt32Slot(0, initSubgraphIndex, 0)
def CallOnceOptionsEnd(builder): return builder.EndObject()


class CallOnceOptionsT(object):

    # CallOnceOptionsT
    def __init__(self):
        self.initSubgraphIndex = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        callOnceOptions = CallOnceOptions()
        callOnceOptions.Init(buf, pos)
        return cls.InitFromObj(callOnceOptions)

    @classmethod
    def InitFromObj(cls, callOnceOptions):
        x = CallOnceOptionsT()
        x._UnPack(callOnceOptions)
        return x

    # CallOnceOptionsT
    def _UnPack(self, callOnceOptions):
        if callOnceOptions is None:
            return
        self.initSubgraphIndex = callOnceOptions.InitSubgraphIndex()

    # CallOnceOptionsT
    def Pack(self, builder):
        CallOnceOptionsStart(builder)
        CallOnceOptionsAddInitSubgraphIndex(builder, self.initSubgraphIndex)
        callOnceOptions = CallOnceOptionsEnd(builder)
        return callOnceOptions
