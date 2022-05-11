# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PoolAttribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PoolAttribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPoolAttribute(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def PoolAttributeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # PoolAttribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PoolAttribute
    def Pad(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # PoolAttribute
    def PadAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # PoolAttribute
    def PadLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PoolAttribute
    def PadIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # PoolAttribute
    def Kernel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # PoolAttribute
    def KernelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # PoolAttribute
    def KernelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PoolAttribute
    def KernelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # PoolAttribute
    def Stride(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # PoolAttribute
    def StrideAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # PoolAttribute
    def StrideLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PoolAttribute
    def StrideIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def Start(builder): builder.StartObject(3)
def PoolAttributeStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddPad(builder, pad): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(pad), 0)
def PoolAttributeAddPad(builder, pad):
    """This method is deprecated. Please switch to AddPad."""
    return AddPad(builder, pad)
def StartPadVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PoolAttributeStartPadVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartPadVector(builder, numElems)
def AddKernel(builder, kernel): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(kernel), 0)
def PoolAttributeAddKernel(builder, kernel):
    """This method is deprecated. Please switch to AddKernel."""
    return AddKernel(builder, kernel)
def StartKernelVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PoolAttributeStartKernelVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartKernelVector(builder, numElems)
def AddStride(builder, stride): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(stride), 0)
def PoolAttributeAddStride(builder, stride):
    """This method is deprecated. Please switch to AddStride."""
    return AddStride(builder, stride)
def StartStrideVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PoolAttributeStartStrideVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStrideVector(builder, numElems)
def End(builder): return builder.EndObject()
def PoolAttributeEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)