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

class TopKV2Options(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTopKV2Options(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TopKV2Options()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def TopKV2OptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # TopKV2Options
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def TopKV2OptionsStart(builder): builder.StartObject(0)
def TopKV2OptionsEnd(builder): return builder.EndObject()


class TopKV2OptionsT(object):

    # TopKV2OptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        topKV2Options = TopKV2Options()
        topKV2Options.Init(buf, pos)
        return cls.InitFromObj(topKV2Options)

    @classmethod
    def InitFromObj(cls, topKV2Options):
        x = TopKV2OptionsT()
        x._UnPack(topKV2Options)
        return x

    # TopKV2OptionsT
    def _UnPack(self, topKV2Options):
        if topKV2Options is None:
            return

    # TopKV2OptionsT
    def Pack(self, builder):
        TopKV2OptionsStart(builder)
        topKV2Options = TopKV2OptionsEnd(builder)
        return topKV2Options
