# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CustomAttribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CustomAttribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCustomAttribute(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def CustomAttributeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # CustomAttribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CustomAttribute
    def Identifier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CustomAttribute
    def Config(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CustomAttribute
    def ImplementationAttrs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # CustomAttribute
    def ImplementationAttrsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # CustomAttribute
    def ImplementationAttrsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CustomAttribute
    def ImplementationAttrsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def CustomAttributeStart(builder): builder.StartObject(3)
def Start(builder):
    return CustomAttributeStart(builder)
def CustomAttributeAddIdentifier(builder, identifier): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(identifier), 0)
def AddIdentifier(builder, identifier):
    return CustomAttributeAddIdentifier(builder, identifier)
def CustomAttributeAddConfig(builder, config): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(config), 0)
def AddConfig(builder, config):
    return CustomAttributeAddConfig(builder, config)
def CustomAttributeAddImplementationAttrs(builder, implementationAttrs): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(implementationAttrs), 0)
def AddImplementationAttrs(builder, implementationAttrs):
    return CustomAttributeAddImplementationAttrs(builder, implementationAttrs)
def CustomAttributeStartImplementationAttrsVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartImplementationAttrsVector(builder, numElems):
    return CustomAttributeStartImplementationAttrsVector(builder, numElems)
def CustomAttributeEnd(builder): return builder.EndObject()
def End(builder):
    return CustomAttributeEnd(builder)