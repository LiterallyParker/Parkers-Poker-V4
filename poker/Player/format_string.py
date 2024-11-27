from Hand import format_string as format_hand

def format_string(Player):
    return (
f"""{"-"*30}\n{Player['name']:^30}
{f"({Player['status']})":^30}\n
{"Chips:":^30}
{Player['chips']:^30}\n
{"Current Bet:":^30}
{Player['current_bet']:^30}\n
{format_hand(Player['hand']):^30}
"""
    )