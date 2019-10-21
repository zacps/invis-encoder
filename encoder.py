#!/usr/bin/env python3
import gzip
import os
import sys

if len(sys.argv) != 3:
    print("Expected two arguments, in file and out file")
    sys.exit(1)
FILE = sys.argv[1]
OUT = sys.argv[2]

print('Opening file')
print(f'File length: {os.stat(FILE).st_size} bytes')
with open(FILE, encoding='utf8') as file:

    print('Compressing text')
    compressed = file.read()

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

print('Encoding')
encoder = Dencoder(ALPHABET)
encoded = []
for byte in compressed:
    encoded.append(encoder.encode(ord(byte)))

print('Consistence check')
for i, byte in enumerate(encoded):
    assert chr(encoder.decode(byte)) == compressed[i]

print('Writing encoded file to out.txt')
with open(OUT, 'w', encoding='utf8') as out:
    out.write(NULL.join(encoded))
print(f'File length: {os.stat(OUT).st_size} bytes')
