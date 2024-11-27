from .extract_one import extract_one

def extract_many(card_bytes: list):
    """Decodes a list of card numbers into readable suits and ranks

    Args:
        nums (list): List of card nums

    Returns:
        extracted_cards: a list containing tuples, (card_bits, suit_bits, rank_bits)
    """
    # Initialize extracted cards array
    extracted_cards = []
    # Iterate over 
    for card_byte in card_bytes:
        extracted_cards.append(extract_one(card_byte))
    return extracted_cards