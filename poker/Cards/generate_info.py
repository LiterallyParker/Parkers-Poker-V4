from Global import RANKS
from .extract_many import extract_many

def generate_info(card_bytes: list):
    """Takes in an array of card bytes
    Returns two dictionaries for ranks and suits, and a set of values

    Args:
        card_bytes (list): List of encoded card bytes
        
    Returns:
        ranks: { '2': 2, '4': 2, '9': 1, 'Jack': 1, 'Ace': 1 }
        suits: { 'Clubs': 3, 'Diamonds': 2, 'Hearts': 1, 'Spades': 1 }
        values: [ 14, 11, 9, 4, 2 ]
    """
    # Decode array of cards
    decoded_cards = extract_many(card_bytes)
    
    # Initialize dictionaries and list
    ranks = {}
    suits = {}
    values = []
    
    # Iterate over decoded cards
    for _, suit_bits, rank_bits in decoded_cards:
        # If unknown rank
        if rank_bits not in ranks:
            # Add rank
            ranks[rank_bits] = 0
        # Count rank
        ranks[rank_bits] += 1
        # If unknown suit
        if suit_bits not in suits:
            # Add suit
            suits[suit_bits] = 0
        # Count suit
        suits[suit_bits] += 1
        
        # Get value of rank
        rank_value = next(key for key, _ in RANKS.items() if key == rank_bits)
        
        # If ace, add a one to the values. For straight checking.
        if rank_value == 14:
            values.append(1)
        
        # Add to values
        values.append(rank_value)
        
    # Sort the values as a set
    values = sorted(set(values), reverse=True)
    
    return ranks, suits, values