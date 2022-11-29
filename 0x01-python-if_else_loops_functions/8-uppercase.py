#!/usr/bin/python3
def uppercase(str):
    for i in str:
        asc = ord(i)
        convert = asc - 32 if (97 <= asc <= 122) else asc
        print("{:c}".format(covert), end="")
        print()
