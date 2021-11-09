# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tosa

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Version(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Version()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVersion(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def VersionBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x4F\x53\x41", size_prefixed=size_prefixed)

    # Version
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Version
    def _major(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Version
    def _minor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 24

    # Version
    def _patch(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Version
    def _draft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

def Start(builder): builder.StartObject(4)
def VersionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def Add_major(builder, Major): builder.PrependInt32Slot(0, Major, 0)
def VersionAdd_major(builder, Major):
    """This method is deprecated. Please switch to Add_major."""
    return Add_major(builder, Major)
def Add_minor(builder, Minor): builder.PrependInt32Slot(1, Minor, 24)
def VersionAdd_minor(builder, Minor):
    """This method is deprecated. Please switch to Add_minor."""
    return Add_minor(builder, Minor)
def Add_patch(builder, Patch): builder.PrependInt32Slot(2, Patch, 0)
def VersionAdd_patch(builder, Patch):
    """This method is deprecated. Please switch to Add_patch."""
    return Add_patch(builder, Patch)
def Add_draft(builder, Draft): builder.PrependBoolSlot(3, Draft, 1)
def VersionAdd_draft(builder, Draft):
    """This method is deprecated. Please switch to Add_draft."""
    return Add_draft(builder, Draft)
def End(builder): return builder.EndObject()
def VersionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)