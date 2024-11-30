from Hand import format_string as format_hand
from Scoring import format_string as format_score

def format_string(player):
    return (
f"""{player['name']:^30}
{f"{player['chips']}c":^30}\n
{format_score(player['score_index']):^30}
{format_hand(player['hand'])}
{"-"*30}
"""
    )