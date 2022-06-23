#!/usr/bin/env python
import sys

def main():
    for name in sys.argv[1:]:
        print(f"Hello {name}!")

if __name__ == "__main__":
    main()
