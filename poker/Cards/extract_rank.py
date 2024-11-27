from Global import RANKS

def extract_rank(card_byte):
    extracted_rank = card_byte & 0b1111
    return extracted_rank