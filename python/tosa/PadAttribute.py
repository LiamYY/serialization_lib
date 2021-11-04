# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PadAttribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPadAttribute(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PadAttribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def PadAttributeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # PadAttribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PadAttribute
    def Padding(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # PadAttribute
    def PaddingAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # PadAttribute
    def PaddingLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PadAttribute
    def PaddingIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # PadAttribute
    def PadConstInt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PadAttribute
    def PadConstFp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def PadAttributeStart(builder): builder.StartObject(3)
def PadAttributeAddPadding(builder, padding): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(padding), 0)
def PadAttributeStartPaddingVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PadAttributeAddPadConstInt(builder, padConstInt): builder.PrependInt32Slot(1, padConstInt, 0)
def PadAttributeAddPadConstFp(builder, padConstFp): builder.PrependFloat32Slot(2, padConstFp, 0.0)
def PadAttributeEnd(builder): return builder.EndObject()