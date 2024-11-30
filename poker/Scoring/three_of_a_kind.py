from Card import count_ranks, extract_many, compress_many
from ._sorting_key import _sorting_key
def three_of_a_kind(card_bytes):
    """
    Returns a sorted copy of the input cards if conditions for a three of a kind are met

    Args:
        card_bytes (list): list of cards
        
    Returns:
        list: list of card bytes if a three of a kind, ordered
    """
    extracted_cards = extract_many(card_bytes)
    ranks = count_ranks(card_bytes)
    
    three_kind_rank = next((rank for rank, count in ranks.items() if count == 3), None)
    if three_kind_rank:
        three_kind_cards = [card for card in extracted_cards if card[0] == three_kind_rank]
        other_cards = [card for card in extracted_cards if card[0] != three_kind_rank]
        
        sorted_three_kind = sorted(three_kind_cards, key=_sorting_key, reverse=True)
        sorted_other = sorted(other_cards, key=_sorting_key, reverse=True)
        
        sorted_cards = sorted_three_kind + sorted_other
        
        return compress_many(sorted_cards)
    
    return []