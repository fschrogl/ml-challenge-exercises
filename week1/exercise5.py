#!/usr/bin/env python3

#
# Week1 - Python Exercise 3
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
from learntools.python.ex5 import *
print('Setup complete.')

# ######################################################################################################################
# Task 1
# ######################################################################################################################

print("\nTASK 1")

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

# Check your answer
q1.check()

print("\n\n")

# ######################################################################################################################
# Task 2a
# ######################################################################################################################

print("\nTASK 2a")

# [1, 2, 3, 4] > 2
# Results in an error

print("\n\n")

# ######################################################################################################################
# Task 2b
# ######################################################################################################################

print("\nTASK 2b")

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.

    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [num > thresh for num in L]

# Check your answer
q2.check()

print("\n\n")

# ######################################################################################################################
# Task 3
# ######################################################################################################################

print("\nTASK 3")

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    yesterdays_meal = ''
    for meal in meals:
        if yesterdays_meal == meal:
            return True
        else :
            yesterdays_meal = meal
    return False

# Check your answer
q3.check()

print("\n\n")

# ######################################################################################################################
# Task 4
# ######################################################################################################################

print("\nTASK 4")

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    average_net_payout_per_run = []
    for run in n_runs:
        average_net_payout_per_run.append(play_slot_machine() - 1)
    return average_net_payout_per_run

q4.solution()

print("\n\n")
