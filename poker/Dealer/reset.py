from Dealer.generate_shuffled_deck import generate_shuffled_deck

def reset(Dealer):
    Dealer['deck'] = (generate_shuffled_deck()) # new shuffled deck