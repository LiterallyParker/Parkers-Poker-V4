from Player import format_string as format_player
from Hand import format_string as format_hand
def format_string(GameState):
    formatted_players = "\n".join(format_player(player) for player in GameState['players'])
    return (
f"""Players:\n{formatted_players}
{"-"*30}
{"Community:":^30}\n
{format_hand(GameState['community_cards'])}"""
)