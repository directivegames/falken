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

class RangeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRangeOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RangeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def RangeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # RangeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def RangeOptionsStart(builder): builder.StartObject(0)
def RangeOptionsEnd(builder): return builder.EndObject()


class RangeOptionsT(object):

    # RangeOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        rangeOptions = RangeOptions()
        rangeOptions.Init(buf, pos)
        return cls.InitFromObj(rangeOptions)

    @classmethod
    def InitFromObj(cls, rangeOptions):
        x = RangeOptionsT()
        x._UnPack(rangeOptions)
        return x

    # RangeOptionsT
    def _UnPack(self, rangeOptions):
        if rangeOptions is None:
            return

    # RangeOptionsT
    def Pack(self, builder):
        RangeOptionsStart(builder)
        rangeOptions = RangeOptionsEnd(builder)
        return rangeOptions
