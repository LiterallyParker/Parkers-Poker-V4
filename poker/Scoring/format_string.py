from Global import SCORES
from Cards import format_string as format_card
from Hand import format_string as format_hand

def format_string(score):
    return (
f"""{SCORES[score[0]]:^30}
{format_hand(score[1])}
"""
)