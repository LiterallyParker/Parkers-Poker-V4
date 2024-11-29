from Cards import extract_many, compress_many
from ._sorting_key import _sorting_key
def straight(card_bytes):
    """
    Returns a sorted copy of the input cards if conditions for a straight are met

    Args:
        card_bytes (list): list of cards
        
    Returns:
        list: list of card bytes if a straight, ordered
    """
    extracted_cards = extract_many(card_bytes)
    ranks = sorted(set(card[1] for card in extracted_cards), reverse=True)
    
    for i in range(len(ranks) - 4):
        if ranks[i] - ranks[i + 4] == 4:
            
            straight_ranks = set(range(ranks[i+4], ranks[i] + 1))
            straight_cards = []
            other_cards = []
            
            for card in extracted_cards:
                if card[1] in straight_ranks:
                    straight_cards.append(card)
                    straight_ranks.remove(card[1])
                    continue
                other_cards.append(card)
            
            sorted_straight = sorted(straight_cards, key=_sorting_key, reverse=True)
            sorted_other = sorted(other_cards, key=_sorting_key, reverse=True)
            
            sorted_cards = sorted_straight + sorted_other
            
            return compress_many(sorted_cards)
        
    if {14, 2, 3, 4, 5}.issubset(ranks):
        straight_ranks = {14, 2, 3, 4, 5}
        straight_cards = []
        other_cards = []
        for card in extracted_cards:
            if card[1] in straight_ranks:
                straight_cards.append(card)
                straight_ranks.remove(card[1])
                continue
            other_cards.append(card)
        
        sorted_straight = sorted(
            straight_cards,
            key=lambda card: (1 if card[1] == 14 else card[1]), reverse=True)
        sorted_others = sorted(other_cards, key=lambda card: card[1], reverse=True)
        
        sorted_cards = sorted_straight + sorted_others
        
        return compress_many(sorted_cards)

    return []