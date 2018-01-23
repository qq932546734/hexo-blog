from gitdb.util import bin_to_hex
from gitdb.fun import (
    type_id_to_type_map,
    type_to_type_id_map
)


class OInfo(tuple):
    """
    carries information about an object in an ODB, providing information
    about the binary sha of the object, the type_string as well as the
    umcompressed size in bytes.

    It can be accessed using tuple notation and using attribute access
    notation:
        assert dbi[0] == dbi.binsha
        assert dbi[1] == dbi.type
        assert dbi[2] == dbi.size

    The type is designed to be as lightweight as possible
    """

    __slots__ = tuple()

    def __new__(cls, sha, type, size):
        return tuple.__new__(cls, (sha, type, size))

    def __init__(self, *args):
        tuple.__init__(self)

    @property
    def binsha(self):
        return self[0]

    @property
    def hexsha(self):
        return bin_to_hex(self[0])

    @property
    def type(self):
        return self[1]

    @property
    def size(self):
        return self[2]


class OPackInfo(tuple):
    """
    As OInfo, but provides a type_id property to retrieve the numerical
    type id, and does not include a sha.

    Additionally, the pack_offset is the absolute offset into the packfile at
    which all object information is located. The data_offset property points
    to the absolute location in the pack at which that actual data stream
    can be found.
    """

    __slots__ = tuple()

    def __new__(cls, packoffset, type, size):
        return tuple.__new__(cls, (packoffset, type, size))

    def __init__(self, *args):
        tuple.__init__(self)

    @property
    def pack_offset(self):
        return self[0]

    @property
    def type(self):
        return type_id_to_type_map[self[1]]

    @property
    def type_id(self):
        return self[1]

    @property
    def size(self):
        return self[2]


class ODeltaPackInfo(OPackInfo):
    """
    Adds delta specific information.
    Either the 20 byte sha which points to some object in the database,
    or the negative offset from the pack offset, so that
    pack_offset - delta_info yields the pack offset of the base object
    """
    __slots__ = tuple()

    def __new__(cls, packoffset, type, size, delta_info):
        return tuple.__new__(cls, (packoffset, type, size, delta_info))

    @property
    def delta_info(self):
        return self[3]


class OStream(OInfo):
    """
    Base for object streams retrieved from the database, providing additional
    information about the stream.
    Generally, ODB streams are read-only as object are immutable
    """
    __slots__ = tuple()

    def __new__(cls, sha, type, size, stream, *args, **kwargs):
        return tuple.__new__(cls, (sha, type, size, stream))

    def __init__(self, *args, **kwargs):
        tuple.__init__(self)

    def read(self, size=-1):
        return self[3].read(size)

    @property
    def stream(self):
        return self[3]


class ODeltaStream(OStream):

    def __new__(cls, sha, type, size, stream, *args, **kwargs):
        return tuple.__new__(cls, (sha, type, size, stream))

    @property
    def size(self):
        return self[3].size


class OPackStream(OPackInfo):

    __slots__ = tuple()

    def __new__(cls, packoffset, type, size, stream, *args):
        return tuple.__new__(cls, (packoffset, type, size, stream))

    def read(self, size=-1):
        return self[3].read(size)

    @property
    def stream(self):
        return self[3]


class ODeltaPackStream(ODeltaPackInfo):

    __slots__ = tuple()












