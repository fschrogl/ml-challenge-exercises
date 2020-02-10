#!/usr/bin/env python3

#
# Week1 - Python Exercise 1
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
from learntools.python.ex1 import *
print("Setup complete! You're ready to start question 0.")

# ######################################################################################################################
# Task 1
# ######################################################################################################################

print("\nTASK 1")

# GIVEN
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * (radius ** 2)

# Check your answer
q1.check()

print("\n\n")

# ######################################################################################################################
# Task 2
# ######################################################################################################################

print("\nTASK 2")

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

######################################################################

c = a
a = b
b = c

# Check your answer
q2.check()

print("\n\n")

# ######################################################################################################################
# Task 3
# ######################################################################################################################

print("\nTASK 3a")

# GIVEN: 5 - 3 // 2
# Task: Add parentheses so that the expression evaluates to 1

print("Given expression 5 - 3 // 2 = ", 5 - 3 // 2)
print("Evaluation of (5 - 3) // 2 = ", (5 - 3) // 2)

#q3.a.solution()
print("\n")


print("\nTASK 3b")

# GIVEN: 8 - 3 * 2 - 1 + 1
# Task: Add parentheses so that the expression evaluates to 0

print("Given expression 8 - 3 * 2 - 1 + 1 = ", 8 - 3 * 2 - 1 + 1)
print("Evaluation of 8 - (3 * 2) - (1 + 1) = ", 8 - (3 * 2) - (1 + 1))

#q3.b.solution()
print("\n\n")

# ######################################################################################################################
# Task 4
# ######################################################################################################################

print("\nTASK 4")

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) % 3

# Check your answer
q4.check()
