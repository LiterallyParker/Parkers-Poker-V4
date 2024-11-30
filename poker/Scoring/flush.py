from Card import extract_many, count_suits, compress_many
from ._sorting_key import _sorting_key

def flush(card_bytes: list):
    """
    Returns a sorted copy of the input cards if conditions for a flush are met

    Args:
        card_bytes (list): list of compressed card bytes

    Returns:
        list: list of compressed card bytes if a flush, ordered
    """
    extracted_cards = extract_many(card_bytes)
    suits = count_suits(card_bytes)

    flush_suit = next((suit for suit, count in suits.items() if count >= 5), None)

    if flush_suit is not None:
        flush_cards = [card for card in extracted_cards if card[1] == flush_suit]
        
        flush_sorted = sorted(flush_cards, key=_sorting_key, reverse=True)
        
        other_cards = [card for card in extracted_cards if card[1] != flush_suit]
        
        sorted_cards = flush_sorted + other_cards
        
        return compress_many(sorted_cards)

    return []