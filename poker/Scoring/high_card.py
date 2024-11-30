from Card import extract_many, compress_many
from ._sorting_key import _sorting_key

def high_card(card_bytes):
    """
    Sorts an array of card bytes into their high card order

    Args:
        card_bytes (list): list of card bytes, refer to Global/
    """
    extracted_cards = extract_many(card_bytes)
    
    sorted_cards = sorted(extracted_cards, key=_sorting_key, reverse=True)
    
    return compress_many(sorted_cards)