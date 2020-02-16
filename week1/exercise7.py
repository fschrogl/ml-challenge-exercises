#!/usr/bin/env python3

#
# Week1 - Python Exercise 7
#
# Prerequisites:
#   * Python Pandas Library must be installed       pacman -S python-pandas
#   * IPython must be installed                     pacman -S ipython
#   * Leantools Library must be installed           pip3 install git+https://github.com/ML-Challenge/learntools.git
#   * Install mathplotlib                           pacman -S python-matplotlib
#
# Following methods are imported from learntools.core:
#   * qX.check()        to check you solution
#   * qX.hint()         to print a hint for solving the task
#   * qX.solution()     to print the complete solution for the task

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex7 import *
print('Setup complete.')

# ######################################################################################################################
# Task 1
# ######################################################################################################################

print("\nTASK 1")

# Import the jimmy_slots submodule
from learntools.python import jimmy_slots

def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylabel("Balance")
    graph.set_ylim(bottom=0)

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

#q1.solution()

print("\n\n")

# ######################################################################################################################
# Task 2
# ######################################################################################################################

print("\nTASK 2")

# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for item in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
best_items(full_dataset)

print("\n\n")

# ######################################################################################################################
# Task 3
# ######################################################################################################################

print("\nTASK 3")

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    pass


# Check your answer
#q3.check()
q3.solution()

print("\n\n")