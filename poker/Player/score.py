from Cards import generate_info
from Scoring import *
from time import time

def score(Player, community_cards):
    all_cards = Player['hand'] + community_cards
    ranks, suits, values = generate_info(all_cards)
    if royal_flush(suits, values):
        return "Royal Flush"
    elif straight_flush(suits, values):
        return "Straight Flush"
    elif four_of_a_kind(ranks):
        return "Four of a Kind"
    elif full_house(ranks):
        return "Full House"
    elif flush(suits):
        return "Flush"
    elif straight(values):
        return "Straight"
    elif three_of_a_kind(ranks):
        return "Three of a Kind"
    elif two_pair(ranks):
        return "Two Pair"
    elif pair(ranks):
        return "Pair"
    else:
        return "High Card"