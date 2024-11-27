from GameState.reset import reset as reset_game_state
from Dealer.reset import reset as reset_dealer
from Player.reset import reset as reset_player

def start(GameState):
    reset_game_state(GameState)
    reset_dealer(GameState['Dealer'])
    for Player in GameState['Players']:
        reset_player(Player)