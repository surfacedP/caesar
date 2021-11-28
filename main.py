#! python3
# main.py takes command line input and applies Caesar cipher
# Currently only works with lower case letters and uses right shift 1, 2, 3
# TODO: add support for uppercase, numbers and special characters
# TODO: add option to input encryption key

import sys


def caesar():
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

    unenc = " ".join(sys.argv[1:])
    unenc_cnt = 0
    enc = ""
    cipher = [1, 2, 3]
    cipher_cnt = 0

    # Check every character in user input...
    for x in unenc:
        alpha_cnt = 0
        # ...against every character in character list...
        for y in alpha:
            # ...if a match, apply cipher and append to encrypted output.
            if x == alpha[alpha_cnt]:
                # Rotates through character list if using a character at the end of the list.
                if alpha_cnt + cipher[cipher_cnt] >= len(alpha):
                    alpha_cnt = alpha_cnt - len(alpha)

                enc = enc + alpha[alpha_cnt + cipher[cipher_cnt]]
                # Rotate through cipher.
                if cipher_cnt == len(cipher) - 1:
                    cipher_cnt = 0
                else:
                    cipher_cnt = cipher_cnt + 1

            alpha_cnt = alpha_cnt + 1
        unenc_cnt = unenc_cnt + 1

    print("Unencrypted:", unenc, "\nEncrypted:", enc)


if len(sys.argv) > 1:
    caesar()
else:
    print("No input from user")

# Formatted with Black
