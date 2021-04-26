# automatically generated by the FlatBuffers compiler, do not modify

# Copyright (c) 2020-2021, ARM Limited.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TosaGraph(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTosaGraph(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TosaGraph()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def TosaGraphBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # TosaGraph
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TosaGraph
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from tosa.Version import Version
            obj = Version()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TosaGraph
    def Blocks(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from tosa.TosaBasicBlock import TosaBasicBlock
            obj = TosaBasicBlock()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TosaGraph
    def BlocksLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaGraph
    def BlocksIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def TosaGraphStart(builder): builder.StartObject(2)
def TosaGraphAddVersion(builder, version): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(version), 0)
def TosaGraphAddBlocks(builder, blocks): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(blocks), 0)
def TosaGraphStartBlocksVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TosaGraphEnd(builder): return builder.EndObject()
