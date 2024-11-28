from Cards import extract_many, count_suits, compress_many
from ._sorting_key import _sorting_key

def flush(card_bytes: list):
    """
    Returns a list of cards ordered first by flush cards (if any), followed by the other cards.
    The flush cards are sorted by rank in descending order.

    Args:
        card_bytes (list): list of card bytes

    Returns:
        list: a list of card bytes sorted with flush cards first, followed by other cards
    """
    extracted_cards = extract_many(card_bytes)
    suits = count_suits(card_bytes)

    flush_suit = next((suit for suit, count in suits.items() if count >= 5), None)

    if flush_suit is not None:
        flush_cards = [card for card in extracted_cards if card[0] == flush_suit]
        
        flush_sorted = sorted(flush_cards, key=_sorting_key, reverse=True)
        
        other_cards = [card for card in extracted_cards if card[0] != flush_suit]
        
        sorted_cards = flush_sorted + other_cards
        
        return compress_many(sorted_cards)

    return []