#!/usr/bin/env python3

#
# Week1 - Python Exercise 2
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
from learntools.python.ex2 import *
print('Setup complete.')

# ######################################################################################################################
# Task 1
# ######################################################################################################################

print("\nTASK 1")

def round_to_two_places(num):
    # That is a docstring. It's like Javadoc for Python

    """Return the given number rounded to two decimal places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)

# Check your answer
q1.check()

print("\n\n")

# ######################################################################################################################
# Task 2
# ######################################################################################################################

print("\nTASK 2")

value = 123.1475464
roundToNearest100 = round(value, -2)
print("roundToNearest100 = ", roundToNearest100)

# q2.solution()

print("\n\n")

# ######################################################################################################################
# Task 3
# ######################################################################################################################

print("\nTASK 3")


def to_smash(total_candies, num_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between the given number of friends. If num_friends isn't
    given defaults to 3.

    >>> to_smash(91)
    1
    """
    return total_candies % num_friends


# Check your answer
q3.check()

print("\n\n")

# ######################################################################################################################
# Task 4
# ######################################################################################################################

print("\nTASK 4")

# Faulty code 1:
#   ruound_to_two_places(9.9999)
# What will happen:
#   Error due to unknown function (typo)
# Fix:
round_to_two_places(9.9999)

# Faulty code 2:
#   x = -10
#   y = 5
#   # Which of the two variables above has the smallest absolute value?
#   smallest_abs = min(abs(x, y))
# What will happen:
#   Error due to unknown function (abs() only takes one argument)
# Fix:
x = -10
y = 5
smallest_abs = min(abs(x), abs(y))

# Faulty code 3:
#   def f(x):
#   y = abs(x)
#   return y
#
#   print(f(5))
# What will happen:
#   will print 5
def f(x):
    y = abs(x)
    return y

print(f(5))

print("\n\n")
