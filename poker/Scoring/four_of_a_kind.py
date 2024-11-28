from Cards import count_ranks, extract_many, compress_many
from ._sorting_key import _sorting_key

def four_of_a_kind(card_bytes):
    """
    Returns a sorted copy of the input cards if conditions for a Four of a Kind are met

    Args:
        card_bytes (list): list of cards
    """
    extracted_cards = extract_many(card_bytes)
    ranks = count_ranks(card_bytes)
    
    four_kind_rank = next((rank for rank, count in ranks.items() if count == 4), None)
    
    if four_kind_rank:
        four_kind_cards = [card for card in extracted_cards if card[1] == four_kind_rank]
        other_cards = [card for card in extracted_cards if card[1] != four_kind_rank]
        
        sorted_four_kind = sorted(four_kind_cards, key=_sorting_key, reverse=True)
        sorted_other = sorted(other_cards, key=_sorting_key, reverse=True)
        
        sorted_cards = sorted_four_kind + sorted_other
        
        return compress_many(sorted_cards)
    
    return []