from Global import SCORES
from Hand import format_string as format_hand

def format_string(score_index: int):
    """
    Formats the score of a poker hand into a readable string.
    
    Args:
        score (tuple): a tuple containing:
            - score[0] (int): The numeric score index (Global.SCORES)
            - score[1] (list): Ordered list of card bytes, by relevancy
            
    Returns:
        str: A formatted string with the score name and card names in order of hand ranking
    """
    return (
f"""{SCORES[score_index].title():^30}
"""
    )