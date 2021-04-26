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

class MirrorPadOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMirrorPadOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MirrorPadOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def MirrorPadOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # MirrorPadOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MirrorPadOptions
    def Mode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def MirrorPadOptionsStart(builder): builder.StartObject(1)
def MirrorPadOptionsAddMode(builder, mode): builder.PrependInt8Slot(0, mode, 0)
def MirrorPadOptionsEnd(builder): return builder.EndObject()


class MirrorPadOptionsT(object):

    # MirrorPadOptionsT
    def __init__(self):
        self.mode = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        mirrorPadOptions = MirrorPadOptions()
        mirrorPadOptions.Init(buf, pos)
        return cls.InitFromObj(mirrorPadOptions)

    @classmethod
    def InitFromObj(cls, mirrorPadOptions):
        x = MirrorPadOptionsT()
        x._UnPack(mirrorPadOptions)
        return x

    # MirrorPadOptionsT
    def _UnPack(self, mirrorPadOptions):
        if mirrorPadOptions is None:
            return
        self.mode = mirrorPadOptions.Mode()

    # MirrorPadOptionsT
    def Pack(self, builder):
        MirrorPadOptionsStart(builder)
        MirrorPadOptionsAddMode(builder, self.mode)
        mirrorPadOptions = MirrorPadOptionsEnd(builder)
        return mirrorPadOptions
