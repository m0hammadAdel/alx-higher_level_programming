#!/usr/bin/python3
def no_c(my_string):
    new_word = ""

    for i in my_string:
        if (i != 'c' or i != 'C'):
            new_word += i

    return new_word
