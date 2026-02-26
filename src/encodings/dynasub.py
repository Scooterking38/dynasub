import codecs


# ---- Your transformation ----
def transform_source(text: str) -> str:
    # Example: @@("hi") -> print("hi")
    return text.replace("@@", "print")


# ---- Decode (USED FOR SOURCE FILES) ----
def decode(input, errors="strict"):
    text = input.decode("utf-8")
    transformed = transform_source(text)
    return transformed, len(input)


# ---- Encode (required but rarely used) ----
def encode(input, errors="strict"):
    return input.encode("utf-8"), len(input)


class Codec(codecs.Codec):
    encode = encode
    decode = decode


def getregentry():
    return codecs.CodecInfo(
        name="dynasub",
        encode=encode,
        decode=decode,
    )
