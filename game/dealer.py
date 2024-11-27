from card_utils import create_deck, shuffle_deck

class Dealer:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.deck = shuffle_deck(create_deck()) # new shuffled deck
    
    def __str__(self):
        return f"Cards: {self.deck}\n"