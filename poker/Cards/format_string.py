from Global import SUITS, RANKS
from .extract_suit import extract_suit
from .extract_rank import extract_rank

def format_string(card_byte: int):
    suit = SUITS[extract_suit(card_byte)]
    rank = RANKS[extract_rank(card_byte)]
    return f"{rank} of {suit}"