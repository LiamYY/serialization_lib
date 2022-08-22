# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TosaOperator(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TosaOperator()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTosaOperator(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def TosaOperatorBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # TosaOperator
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TosaOperator
    def Op(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # TosaOperator
    def AttributeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # TosaOperator
    def Attribute(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # TosaOperator
    def Inputs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # TosaOperator
    def InputsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaOperator
    def InputsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # TosaOperator
    def Outputs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # TosaOperator
    def OutputsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TosaOperator
    def OutputsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def TosaOperatorStart(builder): builder.StartObject(5)
def Start(builder):
    return TosaOperatorStart(builder)
def TosaOperatorAddOp(builder, op): builder.PrependUint32Slot(0, op, 0)
def AddOp(builder, op):
    return TosaOperatorAddOp(builder, op)
def TosaOperatorAddAttributeType(builder, attributeType): builder.PrependUint8Slot(1, attributeType, 0)
def AddAttributeType(builder, attributeType):
    return TosaOperatorAddAttributeType(builder, attributeType)
def TosaOperatorAddAttribute(builder, attribute): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(attribute), 0)
def AddAttribute(builder, attribute):
    return TosaOperatorAddAttribute(builder, attribute)
def TosaOperatorAddInputs(builder, inputs): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(inputs), 0)
def AddInputs(builder, inputs):
    return TosaOperatorAddInputs(builder, inputs)
def TosaOperatorStartInputsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartInputsVector(builder, numElems):
    return TosaOperatorStartInputsVector(builder, numElems)
def TosaOperatorAddOutputs(builder, outputs): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(outputs), 0)
def AddOutputs(builder, outputs):
    return TosaOperatorAddOutputs(builder, outputs)
def TosaOperatorStartOutputsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartOutputsVector(builder, numElems):
    return TosaOperatorStartOutputsVector(builder, numElems)
def TosaOperatorEnd(builder): return builder.EndObject()
def End(builder):
    return TosaOperatorEnd(builder)