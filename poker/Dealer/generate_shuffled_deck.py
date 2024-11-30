def generate_shuffled_deck():
    """
    Creates a shuffled array of 52 numbers, the bits represent cards.
    first 2 bits - suit
    last 4 bits - rank
    00 - Clubs
    01 - Diamonds
    10 - Hearts
    11 - Spades
    0010 - 2
    0011 - 3
    0100 - 4
    0101 - 5
    0110 - 6
    0111 - 7
    1000 - 8
    1001 - 9
    1010 - 10
    1011 - J
    1100 - Q
    1101 - K
    1110 - A
    44 - 101100 - Q of H
    """
    deck = []
    for suit in range(4):
        for rank in range(2, 15):
            card = (rank << 2) | suit
            deck.append(card)
    import random
    random.shuffle(deck)
    return deck