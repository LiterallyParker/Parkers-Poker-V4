from Global import SUITS

def extract_suit(card_byte):
    extracted_suit = card_byte & 0b11
    return extracted_suit