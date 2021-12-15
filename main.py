#! python3
# main.py takes command line input and applies Caesar cipher
# Currently only works with lower case letters and uses right shift 1, 2, 3
# TODO: add support for uppercase, numbers and special characters
# TODO: add option to input encryption key


import sys

char_list = [
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

full_key = [0, 1, 2]

key_id = 0


def rotate_cipher():
    global key_id, full_key

    if key_id == len(full_key) - 1:

        key_id = 0

    else:

        key_id = key_id + 1


def cipher(char_id):
    global key_id, char_list, full_key

    cipher_id = char_id + full_key[key_id]

    if cipher_id >= len(char_list):
        cipher_id = cipher_id - len(char_list)

    otpt = char_list[cipher_id]

    rotate_cipher()

    return otpt


def get_char_id(x):
    global char_list

    char_id = 0

    for y in char_list:

        if x == y:
            return char_id

        char_id = char_id + 1


def caesar(inpt):
    otpt = ""

    for x in inpt:
        char_id = get_char_id(x)

        otpt = otpt + cipher(char_id)

    return otpt


if len(sys.argv) > 1:

    inpt = " ".join(sys.argv[1:])

    print(caesar(inpt))

else:

    print("No input from user")
