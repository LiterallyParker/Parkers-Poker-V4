from .ranks import RANKS
from .decode_many import decode_many

def generate_info(cards: list):
    """Takes array of cards, [community_cards + Player['hand']]
    Creates 2 sets and 1 list
    ranks = { '2': 2, '4': 2, '9': 1, 'Jack': 1, 'Ace': 1 }
    suits = { 'Clubs': 3, 'Diamonds': 2, 'Hearts': 1, 'Spades': 1 }
    values = [ 2, 2, 4, 4, 9, 11, 14 ]

    Args:
        cards (list): List of encoded cards (e.g., [0b101100, 0b111001, ...])
        
    Returns:
        dict: Contains 'ranks', 'suits', 'values'
    """
    decoded_cards = decode_many(cards)
    
    ranks = {}
    suits = {}
    values = []
    
    for _, suit, rank in decoded_cards:
        if rank not in ranks:
            ranks[rank] = 0
        ranks[rank] += 1
        if suit not in suits:
            suits[suit] = 0
        suits[suit] += 1
        
        rank_value = next(key for key, name in RANKS.items() if name == rank)
        values.append(rank_value)
    
    values.sort(reverse=True)
    
    return {
        'ranks':ranks,
        'suits':suits,
        'values':values
    }