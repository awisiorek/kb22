#!/usr/bin/env python3
import sys

for c in sys.stdin.read():
    print(f"{c} U+{ord(c):04X}", end=" ")
    bs = c.encode(encoding='UTF-8')
    for b in bs:
        print(f"{b:02x}", end="")
    print()
