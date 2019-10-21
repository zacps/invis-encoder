#!/usr/bin/env python3
import sys
import gzip

if len(sys.argv) != 3:
    print("Expected two arguments, in file and out file")
    sys.exit(1)
FILE = sys.argv[1]
OUT = sys.argv[2]

# Taken from https://en.wikipedia.org/wiki/Whitespace_character#Unicode
ALPHABET = "\u200B\u200C\u200D\u2060\uFEFF"
NULL = "\u180E"

# From https://github.com/yamatt/python-dencoder
class Dencoder():
    def __init__(self, alphabet):
        """
        Set up the decoder/encoder alphabet.
        """
        self.alphabet = alphabet
        self.base = len(self.alphabet)

    def encode(self, number):
        """
        Turns a number in to a string that represents it.
        """
        if number == 0:
            return self.alphabet[0]
        s = ''
        while number > 0:
            s += self.alphabet[number % self.base]
            number = number // self.base

        return s[::-1] # reverse string

    def decode(self, s):
        """
        Turns string encoding back in to a number.
        """
        i = 0
        for char in s:
            i = i * self.base + self.alphabet.index(char)
        return i

decoder = Dencoder(ALPHABET)

print('Decoding')
new = open(FILE, 'r', encoding='utf8')
encoded = new.read().split(NULL)
decoded = []
for i, s in enumerate(encoded):
    d = decoder.decode(s)
    decoded.append(chr(d))

print('Decompressing')
decompressed = "".join(decoded)
with open(OUT, 'w') as decompressed_f:
    decompressed_f.write(decompressed)
