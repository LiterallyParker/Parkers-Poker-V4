from .extract_many import extract_many

def count_suits(card_bytes):
    extracted_cards = extract_many(card_bytes)
    suits = {}
    for suit_bits, _ in extracted_cards:
        if suit_bits not in suits:
            suits[suit_bits] = 0
        suits[suit_bits] += 1
        
    return suits