from Cards import decode_many
from Player import format_string as format_player
from Dealer import format_string as format_dealer

def format_string(GameState):
    formatted_players = "\n".join(format_player(player) for player in GameState['Players'])
    return (
f"""Players:\n{formatted_players}
Community: {decode_many(GameState['community_cards'])}\n
Deck:\n{format_dealer(GameState['Dealer'])}"""
)