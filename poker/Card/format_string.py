from Global import RANKS, SUITS
from colorama import Fore
from .extract_rank import extract_rank
from .extract_suit import extract_suit

def format_string(card_byte: int):
    rank = RANKS[extract_rank(card_byte)]
    suit = SUITS[extract_suit(card_byte)]
    return f"{rank.title()} of {suit.title()}"