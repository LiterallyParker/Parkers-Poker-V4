from dealer import Dealer
from output_string import output_string

class GameState:
    def __init__(self, players=[]):
        self.players = players
        self.dealer = Dealer()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        self.round = 'pre-flop'
        self.betting_round_over = False