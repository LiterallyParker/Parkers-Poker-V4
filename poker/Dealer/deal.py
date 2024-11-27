def deal(Dealer, Player, num=1):
    """Deals n cards from GameState Dealer hand to cards array

    Args:
        Dealer (dict): Dealer object.
        cards (list): card array, usually Player['hand'].
        num (int, optional): Amount to deal. Defaults to 1.
    """
    Player['hand'].extend([Dealer['deck'].pop() for _ in range(num)])