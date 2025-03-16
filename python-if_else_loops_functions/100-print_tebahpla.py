#!/usr/bin/python3
for i in range(25, -1, -1):
    print(chr(122 - i) if i % 2 == 0 else chr(90 - i), end="")
