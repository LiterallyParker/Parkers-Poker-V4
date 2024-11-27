from Global import SCORES
from Cards import format_string as format_card

def format_string(score):
    return (
f"""{SCORES[score]:^30}
"""
)