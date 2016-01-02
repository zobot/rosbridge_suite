import zlib
from base64 import standard_b64encode, standard_b64decode
from StringIO import StringIO
from math import floor, ceil, sqrt


def encode(string):
    """ gzip compression on the data stored in a string, return the b64 encoded bytes """
    enc_string = zlib.compress(string)
    encoded = standard_b64encode(enc_string)
    return encoded

def decode(string):
    """ b64 decode the string, then gzip-decompress """
    decoded = standard_b64decode(string)
    return zlib.decompress(decoded)
