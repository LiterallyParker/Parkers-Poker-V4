from .get_rank import get_rank
from .get_suit import get_suit

def decode_one(card):
    suit_bits = card >> 4 # First two bits
    rank_bits = card & 0xF # Last 4 bits
    suit = get_suit(suit_bits)
    rank = get_rank(rank_bits)
    return card, suit, rank