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

class FullyConnectedOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFullyConnectedOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FullyConnectedOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def FullyConnectedOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # FullyConnectedOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FullyConnectedOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # FullyConnectedOptions
    def WeightsFormat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # FullyConnectedOptions
    def KeepNumDims(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # FullyConnectedOptions
    def AsymmetricQuantizeInputs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def FullyConnectedOptionsStart(builder): builder.StartObject(4)
def FullyConnectedOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def FullyConnectedOptionsAddWeightsFormat(builder, weightsFormat): builder.PrependInt8Slot(1, weightsFormat, 0)
def FullyConnectedOptionsAddKeepNumDims(builder, keepNumDims): builder.PrependBoolSlot(2, keepNumDims, 0)
def FullyConnectedOptionsAddAsymmetricQuantizeInputs(builder, asymmetricQuantizeInputs): builder.PrependBoolSlot(3, asymmetricQuantizeInputs, 0)
def FullyConnectedOptionsEnd(builder): return builder.EndObject()


class FullyConnectedOptionsT(object):

    # FullyConnectedOptionsT
    def __init__(self):
        self.fusedActivationFunction = 0  # type: int
        self.weightsFormat = 0  # type: int
        self.keepNumDims = False  # type: bool
        self.asymmetricQuantizeInputs = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        fullyConnectedOptions = FullyConnectedOptions()
        fullyConnectedOptions.Init(buf, pos)
        return cls.InitFromObj(fullyConnectedOptions)

    @classmethod
    def InitFromObj(cls, fullyConnectedOptions):
        x = FullyConnectedOptionsT()
        x._UnPack(fullyConnectedOptions)
        return x

    # FullyConnectedOptionsT
    def _UnPack(self, fullyConnectedOptions):
        if fullyConnectedOptions is None:
            return
        self.fusedActivationFunction = fullyConnectedOptions.FusedActivationFunction()
        self.weightsFormat = fullyConnectedOptions.WeightsFormat()
        self.keepNumDims = fullyConnectedOptions.KeepNumDims()
        self.asymmetricQuantizeInputs = fullyConnectedOptions.AsymmetricQuantizeInputs()

    # FullyConnectedOptionsT
    def Pack(self, builder):
        FullyConnectedOptionsStart(builder)
        FullyConnectedOptionsAddFusedActivationFunction(builder, self.fusedActivationFunction)
        FullyConnectedOptionsAddWeightsFormat(builder, self.weightsFormat)
        FullyConnectedOptionsAddKeepNumDims(builder, self.keepNumDims)
        FullyConnectedOptionsAddAsymmetricQuantizeInputs(builder, self.asymmetricQuantizeInputs)
        fullyConnectedOptions = FullyConnectedOptionsEnd(builder)
        return fullyConnectedOptions
