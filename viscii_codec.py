import codecs
from functools import lru_cache

# Codec APIs


class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


# encodings module API


@lru_cache()
def getregentry():
    return codecs.CodecInfo(
        name="viscii",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


# Decoding Table

decoding_table = (
    "\x00\x01Ẳ\x03\x04ẴẪ\x07\x08\t\n\x0b\x0c\r\x0e\x0f"
    "\x10\x11\x12\x13Ỷ\x15\x16\x17\x18Ỹ\x1a\x1b\x1c\x1dỴ\x1f"
    " !\"#$%&'()*+,-./"
    "0123456789:;<=>?"
    "@ABCDEFGHIJKLMNO"
    "PQRSTUVWXYZ[\\]^_"
    "`abcdefghijklmno"
    "pqrstuvwxyz{|}~\x7f"
    "ẠẮẰẶẤẦẨẬẼẸẾỀỂỄỆỐ"
    "ỒỔỖỘỢỚỜỞỊỎỌỈỦŨỤỲ"
    "Õắằặấầẩậẽẹếềểễệố"
    "ồổỗỠƠộờởịỰỨỪỬơớƯ"
    "ÀÁÂÃẢĂẳẵÈÉÊẺÌÍĨỳ"
    "ĐứÒÓÔạỷừửÙÚỹỵÝỡư"
    "àáâãảăữẫèéêẻìíĩỉ"
    "đựòóôõỏọụùúũủýợỮ"
)

# Encoding table
encoding_table = codecs.charmap_build(decoding_table)


def search_function(encoding):
    entry = getregentry()

    if entry.name == encoding:
        return entry

    return None


def register():
    codecs.register(search_function)


def unregister():
    try:
        codecs.unregister(search_function)
    except AttributeError:
        pass
