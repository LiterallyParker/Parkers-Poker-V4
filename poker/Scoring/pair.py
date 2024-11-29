from Cards import count_ranks, extract_many, compress_many
from ._sorting_key import _sorting_key

def pair(card_bytes):
    """
    Returns a sorted copy of the input cards if conditions for a pair are met

    Args:
        card_bytes (list): list of cards
        
    Returns:
        list: list of card bytes if a pair, ordered
    """
    extracted_cards = extract_many(card_bytes)
    ranks = count_ranks(card_bytes)
    
    pair_rank = next((rank for rank, count in ranks.items() if count == 2), None)
    if pair_rank is None:
        return []
    
    pair_cards = [card for card in extracted_cards if card[1] == pair_rank]
    other_cards = [card for card in extracted_cards if card[1] != pair_rank]
    
    sorted_pair = sorted(pair_cards, key=_sorting_key, reverse=True)
    sorted_other = sorted(other_cards, key=_sorting_key, reverse=True)
    
    sorted_cards = sorted_pair + sorted_other
    
    return compress_many(sorted_cards)