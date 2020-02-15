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
from learntools.python.ex4 import *
print('Setup complete.')

# ######################################################################################################################
# Task 1
# ######################################################################################################################

print("\nTASK 1")

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    return L[1] if len(L) >= 2 else None

# Check your answer
q1.check()

print("\n\n")

# ######################################################################################################################
# Task 2
# ######################################################################################################################

print("\nTASK 2")

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1] if len(teams[-1]) >= 1 else None

# Check your answer
q2.check()

print("\n\n")

# ######################################################################################################################
# Task 3
# ######################################################################################################################

print("\nTASK 3")

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.

    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]

# Check your answer
q3.check()

print("\n\n")

# ######################################################################################################################
# Task 4
# ######################################################################################################################

print("\nTASK 4")

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

# Check your answer
q4.check()

print("\n\n")

# ######################################################################################################################
# Task 5
# ######################################################################################################################

print("\nTASK 5")

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    not_last_arrival = (name != arrivals[-1])
    name_index = arrivals.index(name)
    late_index = ((len(arrivals) // 2) + (len(arrivals) % 2 > 0))
    return not_last_arrival and name_index >= late_index

# Check your answer
q5.check()

print("\n\n")
