def flip(GameState, num=1):
    """Deals n cards from GameState Dealer hand to community_cards

    Args:
        Dealer (dict): Dealer object.
        cards (list): card array, usually Player['hand'].
        num (int, optional): Amount to deal. Defaults to 1.
    """
    GameState['community_cards'].extend([GameState['dealer']['deck'].pop() for _ in range(num)])