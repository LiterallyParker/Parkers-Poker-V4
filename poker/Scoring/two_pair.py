from Card import count_ranks, extract_many, compress_many
from ._sorting_key import _sorting_key

def two_pair(card_bytes):
    """
    Returns a sorted copy of the input cards if conditions for a two pair are met

    Args:
        card_bytes (list): list of cards
        
    Returns:
        list: list of card bytes if a two pair, ordered
    """
    extracted_cards = extract_many(card_bytes)
    ranks = count_ranks(card_bytes)
    
    pair_ranks = [rank for rank, count in ranks.items() if count == 2]
    
    if len(pair_ranks) < 2:
        return []
    
    top_two_pairs = sorted(pair_ranks, reverse=True)[:2]
    
    pair_cards = [card for card in extracted_cards if card[0] in top_two_pairs]
    other_cards = [card for card in extracted_cards if card[0] not in top_two_pairs]
    
    sorted_pairs = sorted(pair_cards, key=_sorting_key, reverse=True)
    sorted_other = sorted(other_cards, key=_sorting_key, reverse=True)
    
    sorted_cards = sorted_pairs + sorted_other
    
    return compress_many(sorted_cards)