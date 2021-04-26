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

class EmbeddingLookupSparseOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEmbeddingLookupSparseOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EmbeddingLookupSparseOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def EmbeddingLookupSparseOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # EmbeddingLookupSparseOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EmbeddingLookupSparseOptions
    def Combiner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def EmbeddingLookupSparseOptionsStart(builder): builder.StartObject(1)
def EmbeddingLookupSparseOptionsAddCombiner(builder, combiner): builder.PrependInt8Slot(0, combiner, 0)
def EmbeddingLookupSparseOptionsEnd(builder): return builder.EndObject()


class EmbeddingLookupSparseOptionsT(object):

    # EmbeddingLookupSparseOptionsT
    def __init__(self):
        self.combiner = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        embeddingLookupSparseOptions = EmbeddingLookupSparseOptions()
        embeddingLookupSparseOptions.Init(buf, pos)
        return cls.InitFromObj(embeddingLookupSparseOptions)

    @classmethod
    def InitFromObj(cls, embeddingLookupSparseOptions):
        x = EmbeddingLookupSparseOptionsT()
        x._UnPack(embeddingLookupSparseOptions)
        return x

    # EmbeddingLookupSparseOptionsT
    def _UnPack(self, embeddingLookupSparseOptions):
        if embeddingLookupSparseOptions is None:
            return
        self.combiner = embeddingLookupSparseOptions.Combiner()

    # EmbeddingLookupSparseOptionsT
    def Pack(self, builder):
        EmbeddingLookupSparseOptionsStart(builder)
        EmbeddingLookupSparseOptionsAddCombiner(builder, self.combiner)
        embeddingLookupSparseOptions = EmbeddingLookupSparseOptionsEnd(builder)
        return embeddingLookupSparseOptions
