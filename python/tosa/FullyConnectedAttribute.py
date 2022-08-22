# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FullyConnectedAttribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FullyConnectedAttribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFullyConnectedAttribute(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def FullyConnectedAttributeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # FullyConnectedAttribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FullyConnectedAttribute
    def InputZp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FullyConnectedAttribute
    def WeightZp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def FullyConnectedAttributeStart(builder): builder.StartObject(2)
def Start(builder):
    return FullyConnectedAttributeStart(builder)
def FullyConnectedAttributeAddInputZp(builder, inputZp): builder.PrependInt32Slot(0, inputZp, 0)
def AddInputZp(builder, inputZp):
    return FullyConnectedAttributeAddInputZp(builder, inputZp)
def FullyConnectedAttributeAddWeightZp(builder, weightZp): builder.PrependInt32Slot(1, weightZp, 0)
def AddWeightZp(builder, weightZp):
    return FullyConnectedAttributeAddWeightZp(builder, weightZp)
def FullyConnectedAttributeEnd(builder): return builder.EndObject()
def End(builder):
    return FullyConnectedAttributeEnd(builder)