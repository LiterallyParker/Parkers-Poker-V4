from Game.reset import reset as reset_game_state
from Dealer.reset import reset as reset_dealer
from Player.reset import reset as reset_player

def start(GameState):
    reset_game_state(GameState)
    reset_dealer(GameState['dealer'])
    for Player in GameState['players']:
        reset_player(Player)