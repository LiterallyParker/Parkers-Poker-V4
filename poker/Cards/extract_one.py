from .extract_rank import extract_rank
from .extract_suit import extract_suit
from .format_string import format_string

def extract_one(card_byte):
    suit_byte = extract_suit(card_byte)
    rank_byte = extract_rank(card_byte)
    extracted_card = (suit_byte, rank_byte)
    return extracted_card