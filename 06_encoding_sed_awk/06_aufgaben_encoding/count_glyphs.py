#!/usr/bin/env python3
import unicodedata
import sys

# nfc = unicodedata.normalize('NFC', sys.stdin.read())
# print(len(nfc))

count = 0
other = 0
for chr in sys.stdin.read():
    x = unicodedata.combining(chr)
    if x == 0:
        count += 1
    else: 
        other += 1
print("Buchstaben: ", count)
print("kombinierende Zeichen: ", other)