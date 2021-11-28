#! python3
# main.py takes command line input and applies Caesar cipher
# Currently only works with lower case letters and uses right shift of 1
# TODO: add support for uppercase, numbers and special characters
# TODO: add option to input encryption key

import sys

alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

if len(sys.argv) > 1:
    unenc = " ".join(sys.argv[1:])
    cnt1 = 0
    enc = ""

    for x in unenc:
        cnt2 = 0
        for y in alpha:
            if x == alpha[cnt2]:
                enc = enc + alpha[cnt2 + 1]
            cnt2 = cnt2 + 1
        cnt1 = cnt1 + 1

    print("Unencrypted:", unenc, "\nEncrypted:", enc)

# Formatted with Black
