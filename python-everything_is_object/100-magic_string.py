#!/usr/bin/python3
def magic_string(n):
    return ''.join(['BestSchool' * i for i in range(1, n+1)])
print(magic_string(n))
