#!/usr/bin/env python3

#
# Week1 - Python Exercise 6
#
# Prerequisites:
#   * Python Pandas Library must be installed       pacman -S python-pandas
#   * IPython must be installed                     pacman -S ipython
#   * Leantools Library must be installed           pip3 install git+https://github.com/ML-Challenge/learntools.git
#
# Following methods are imported from learntools.core:
#   * qX.check()        to check you solution
#   * qX.hint()         to print a hint for solving the task
#   * qX.solution()     to print the complete solution for the task

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *
print('Setup complete.')

# ######################################################################################################################
# Task 1
# ######################################################################################################################

print("\nTASK 1")

a = ""
length = 0
q0.a.check()

b = "it's ok"
length = 7
q0.b.check()

c = 'it\'s ok'
length = 7
q0.c.check()

d = """hey"""
length = 3
q0.d.check()

e = '\n'
length = 1
q0.e.check()

print("\n\n")

# ######################################################################################################################
# Task 2
# ######################################################################################################################

print("\nTASK 2")

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code) == 5 and zip_code.isdigit()

# Check your answer
q1.check()

print("\n\n")

# ######################################################################################################################
# Task 3
# ######################################################################################################################

print("\nTASK 3")

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    valid_index_list = []
    for index in range(len(doc_list)):
        doc_with_spaces = " " + doc_list[index] + " "
        find_index = doc_with_spaces.lower().replace('.', ' ').replace(',', ' ').find(" " + keyword + " ")
        if find_index > -1:
            valid_index_list.append(index)
    return valid_index_list

# Check your answer
q2.check()

print("\n\n")

# ######################################################################################################################
# Task 4
# ######################################################################################################################

print("\nTASK 4")

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    valid_index_map = {keyword: [] for keyword in keywords}
    for keyword in keywords:
        for index in range(len(doc_list)):
            doc_with_spaces = " " + doc_list[index] + " "
            find_index = doc_with_spaces.lower().replace('.', ' ').replace(',', ' ').find(" " + keyword + " ")
            if find_index > -1:
                valid_index_map[keyword].append(index)
    return valid_index_map

# Check your answer
q3.check()

print("\n\n")
