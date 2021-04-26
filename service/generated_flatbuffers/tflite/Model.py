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

class Model(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsModel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Model()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def ModelBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # Model
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Model
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Model
    def OperatorCodes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.OperatorCode import OperatorCode
            obj = OperatorCode()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def OperatorCodesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def OperatorCodesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Model
    def Subgraphs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.SubGraph import SubGraph
            obj = SubGraph()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def SubgraphsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def SubgraphsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Model
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Model
    def Buffers(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.Buffer import Buffer
            obj = Buffer()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def BuffersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def BuffersIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # Model
    def MetadataBuffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Model
    def MetadataBufferAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Model
    def MetadataBufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def MetadataBufferIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Model
    def Metadata(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.Metadata import Metadata
            obj = Metadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def MetadataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def MetadataIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # Model
    def SignatureDefs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tflite.SignatureDef import SignatureDef
            obj = SignatureDef()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Model
    def SignatureDefsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Model
    def SignatureDefsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

def ModelStart(builder): builder.StartObject(8)
def ModelAddVersion(builder, version): builder.PrependUint32Slot(0, version, 0)
def ModelAddOperatorCodes(builder, operatorCodes): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(operatorCodes), 0)
def ModelStartOperatorCodesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ModelAddSubgraphs(builder, subgraphs): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(subgraphs), 0)
def ModelStartSubgraphsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ModelAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def ModelAddBuffers(builder, buffers): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(buffers), 0)
def ModelStartBuffersVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ModelAddMetadataBuffer(builder, metadataBuffer): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(metadataBuffer), 0)
def ModelStartMetadataBufferVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ModelAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def ModelStartMetadataVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ModelAddSignatureDefs(builder, signatureDefs): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(signatureDefs), 0)
def ModelStartSignatureDefsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ModelEnd(builder): return builder.EndObject()

import tflite.Buffer
import tflite.Metadata
import tflite.OperatorCode
import tflite.SignatureDef
import tflite.SubGraph
try:
    from typing import List
except:
    pass

class ModelT(object):

    # ModelT
    def __init__(self):
        self.version = 0  # type: int
        self.operatorCodes = None  # type: List[tflite.OperatorCode.OperatorCodeT]
        self.subgraphs = None  # type: List[tflite.SubGraph.SubGraphT]
        self.description = None  # type: str
        self.buffers = None  # type: List[tflite.Buffer.BufferT]
        self.metadataBuffer = None  # type: List[int]
        self.metadata = None  # type: List[tflite.Metadata.MetadataT]
        self.signatureDefs = None  # type: List[tflite.SignatureDef.SignatureDefT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        model = Model()
        model.Init(buf, pos)
        return cls.InitFromObj(model)

    @classmethod
    def InitFromObj(cls, model):
        x = ModelT()
        x._UnPack(model)
        return x

    # ModelT
    def _UnPack(self, model):
        if model is None:
            return
        self.version = model.Version()
        if not model.OperatorCodesIsNone():
            self.operatorCodes = []
            for i in range(model.OperatorCodesLength()):
                if model.OperatorCodes(i) is None:
                    self.operatorCodes.append(None)
                else:
                    operatorCode_ = tflite.OperatorCode.OperatorCodeT.InitFromObj(model.OperatorCodes(i))
                    self.operatorCodes.append(operatorCode_)
        if not model.SubgraphsIsNone():
            self.subgraphs = []
            for i in range(model.SubgraphsLength()):
                if model.Subgraphs(i) is None:
                    self.subgraphs.append(None)
                else:
                    subGraph_ = tflite.SubGraph.SubGraphT.InitFromObj(model.Subgraphs(i))
                    self.subgraphs.append(subGraph_)
        self.description = model.Description()
        if not model.BuffersIsNone():
            self.buffers = []
            for i in range(model.BuffersLength()):
                if model.Buffers(i) is None:
                    self.buffers.append(None)
                else:
                    buffer_ = tflite.Buffer.BufferT.InitFromObj(model.Buffers(i))
                    self.buffers.append(buffer_)
        if not model.MetadataBufferIsNone():
            if np is None:
                self.metadataBuffer = []
                for i in range(model.MetadataBufferLength()):
                    self.metadataBuffer.append(model.MetadataBuffer(i))
            else:
                self.metadataBuffer = model.MetadataBufferAsNumpy()
        if not model.MetadataIsNone():
            self.metadata = []
            for i in range(model.MetadataLength()):
                if model.Metadata(i) is None:
                    self.metadata.append(None)
                else:
                    metadata_ = tflite.Metadata.MetadataT.InitFromObj(model.Metadata(i))
                    self.metadata.append(metadata_)
        if not model.SignatureDefsIsNone():
            self.signatureDefs = []
            for i in range(model.SignatureDefsLength()):
                if model.SignatureDefs(i) is None:
                    self.signatureDefs.append(None)
                else:
                    signatureDef_ = tflite.SignatureDef.SignatureDefT.InitFromObj(model.SignatureDefs(i))
                    self.signatureDefs.append(signatureDef_)

    # ModelT
    def Pack(self, builder):
        if self.operatorCodes is not None:
            operatorCodeslist = []
            for i in range(len(self.operatorCodes)):
                operatorCodeslist.append(self.operatorCodes[i].Pack(builder))
            ModelStartOperatorCodesVector(builder, len(self.operatorCodes))
            for i in reversed(range(len(self.operatorCodes))):
                builder.PrependUOffsetTRelative(operatorCodeslist[i])
            operatorCodes = builder.EndVector(len(self.operatorCodes))
        if self.subgraphs is not None:
            subgraphslist = []
            for i in range(len(self.subgraphs)):
                subgraphslist.append(self.subgraphs[i].Pack(builder))
            ModelStartSubgraphsVector(builder, len(self.subgraphs))
            for i in reversed(range(len(self.subgraphs))):
                builder.PrependUOffsetTRelative(subgraphslist[i])
            subgraphs = builder.EndVector(len(self.subgraphs))
        if self.description is not None:
            description = builder.CreateString(self.description)
        if self.buffers is not None:
            bufferslist = []
            for i in range(len(self.buffers)):
                bufferslist.append(self.buffers[i].Pack(builder))
            ModelStartBuffersVector(builder, len(self.buffers))
            for i in reversed(range(len(self.buffers))):
                builder.PrependUOffsetTRelative(bufferslist[i])
            buffers = builder.EndVector(len(self.buffers))
        if self.metadataBuffer is not None:
            if np is not None and type(self.metadataBuffer) is np.ndarray:
                metadataBuffer = builder.CreateNumpyVector(self.metadataBuffer)
            else:
                ModelStartMetadataBufferVector(builder, len(self.metadataBuffer))
                for i in reversed(range(len(self.metadataBuffer))):
                    builder.PrependInt32(self.metadataBuffer[i])
                metadataBuffer = builder.EndVector(len(self.metadataBuffer))
        if self.metadata is not None:
            metadatalist = []
            for i in range(len(self.metadata)):
                metadatalist.append(self.metadata[i].Pack(builder))
            ModelStartMetadataVector(builder, len(self.metadata))
            for i in reversed(range(len(self.metadata))):
                builder.PrependUOffsetTRelative(metadatalist[i])
            metadata = builder.EndVector(len(self.metadata))
        if self.signatureDefs is not None:
            signatureDefslist = []
            for i in range(len(self.signatureDefs)):
                signatureDefslist.append(self.signatureDefs[i].Pack(builder))
            ModelStartSignatureDefsVector(builder, len(self.signatureDefs))
            for i in reversed(range(len(self.signatureDefs))):
                builder.PrependUOffsetTRelative(signatureDefslist[i])
            signatureDefs = builder.EndVector(len(self.signatureDefs))
        ModelStart(builder)
        ModelAddVersion(builder, self.version)
        if self.operatorCodes is not None:
            ModelAddOperatorCodes(builder, operatorCodes)
        if self.subgraphs is not None:
            ModelAddSubgraphs(builder, subgraphs)
        if self.description is not None:
            ModelAddDescription(builder, description)
        if self.buffers is not None:
            ModelAddBuffers(builder, buffers)
        if self.metadataBuffer is not None:
            ModelAddMetadataBuffer(builder, metadataBuffer)
        if self.metadata is not None:
            ModelAddMetadata(builder, metadata)
        if self.signatureDefs is not None:
            ModelAddSignatureDefs(builder, signatureDefs)
        model = ModelEnd(builder)
        return model