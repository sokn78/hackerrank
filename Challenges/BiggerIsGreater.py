import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.


def sort_string(s):
    return "".join(sorted(s))

def biggerIsGreater(w):
    new_word = None
    word_found = False

    for i in range(1, len(w)+1):
        second_half = w[-i:]
        all_greater_chars = [(char, i) for i,char in enumerate(second_half) if char > second_half[0]]

        if len(all_greater_chars) > 0:
            swap_indice = min(all_greater_chars)[1]
            new_word = w[:-i] + second_half[swap_indice] + sort_string(second_half[:swap_indice] + second_half[swap_indice+1:])
            word_found = True
            break

    if word_found:
        return new_word
    else:
        return 'no answer'