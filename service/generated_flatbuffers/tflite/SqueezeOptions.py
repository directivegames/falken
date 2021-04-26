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

class SqueezeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSqueezeOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SqueezeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def SqueezeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SqueezeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SqueezeOptions
    def SqueezeDims(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SqueezeOptions
    def SqueezeDimsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # SqueezeOptions
    def SqueezeDimsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SqueezeOptions
    def SqueezeDimsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def SqueezeOptionsStart(builder): builder.StartObject(1)
def SqueezeOptionsAddSqueezeDims(builder, squeezeDims): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(squeezeDims), 0)
def SqueezeOptionsStartSqueezeDimsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SqueezeOptionsEnd(builder): return builder.EndObject()

try:
    from typing import List
except:
    pass

class SqueezeOptionsT(object):

    # SqueezeOptionsT
    def __init__(self):
        self.squeezeDims = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        squeezeOptions = SqueezeOptions()
        squeezeOptions.Init(buf, pos)
        return cls.InitFromObj(squeezeOptions)

    @classmethod
    def InitFromObj(cls, squeezeOptions):
        x = SqueezeOptionsT()
        x._UnPack(squeezeOptions)
        return x

    # SqueezeOptionsT
    def _UnPack(self, squeezeOptions):
        if squeezeOptions is None:
            return
        if not squeezeOptions.SqueezeDimsIsNone():
            if np is None:
                self.squeezeDims = []
                for i in range(squeezeOptions.SqueezeDimsLength()):
                    self.squeezeDims.append(squeezeOptions.SqueezeDims(i))
            else:
                self.squeezeDims = squeezeOptions.SqueezeDimsAsNumpy()

    # SqueezeOptionsT
    def Pack(self, builder):
        if self.squeezeDims is not None:
            if np is not None and type(self.squeezeDims) is np.ndarray:
                squeezeDims = builder.CreateNumpyVector(self.squeezeDims)
            else:
                SqueezeOptionsStartSqueezeDimsVector(builder, len(self.squeezeDims))
                for i in reversed(range(len(self.squeezeDims))):
                    builder.PrependInt32(self.squeezeDims[i])
                squeezeDims = builder.EndVector(len(self.squeezeDims))
        SqueezeOptionsStart(builder)
        if self.squeezeDims is not None:
            SqueezeOptionsAddSqueezeDims(builder, squeezeDims)
        squeezeOptions = SqueezeOptionsEnd(builder)
        return squeezeOptions
