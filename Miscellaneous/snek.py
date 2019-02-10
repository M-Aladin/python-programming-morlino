"""This module contains miscellaneous functions defined for the sake of exercise"""


def rot13(string):
    """This function takes a string and returns it encoded (or decoded) in ROT13"""
    i = 0    # initialize counter

    lyst = list(string)   # transform string into list to allow item reassignment

    for letter in lyst:

        if letter.isalpha():   # only rotate alphabetic characters

            # rotation:
            a = ord(letter) + 13

            # management of revolving (if after rotation the letter goes "beyond" Z we make it wrap around to the
            # beginning)
            if (letter.isupper() and a > 90) or (letter.islower() and a > 122):
                a = a - 26

            # item reassignment
            lyst[i] = chr(a)

        # increment counter regardless of if branch execution
        i = i + 1

    string = ''.join(lyst)  # reassign the variable string to its new rotated value
    return string


