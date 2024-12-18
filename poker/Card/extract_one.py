from .extract_rank import extract_rank
from .extract_suit import extract_suit

def extract_one(card_byte):
    rank_byte = extract_rank(card_byte)
    suit_byte = extract_suit(card_byte)
    extracted_card = (rank_byte, suit_byte)
    return extracted_card