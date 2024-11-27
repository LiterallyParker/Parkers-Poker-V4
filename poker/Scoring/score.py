from Cards import generate_info, extract_many
from Scoring import *
from time import time

def score(card_bytes):
    # Get sets of ranks, suits, and values
    ranks, suits, values = generate_info(card_bytes)
    # Return score
    if royal_flush(suits, values):
        return 9
    elif straight_flush(suits, values):
        return 8
    elif four_of_a_kind(ranks):
        return 7
    elif full_house(ranks):
        return 6
    elif flush(suits):
        return 5
    elif straight(values):
        return 4
    elif three_of_a_kind(ranks):
        return 3
    elif two_pair(ranks):
        return 2
    elif pair(ranks):
        return 1
    else:
        return 0