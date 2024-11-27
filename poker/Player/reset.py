def reset(Player):
    """
    Resets the Player's attributes for a new round.
    :param Player: Player Object
    """
    Player['status'] = 'active'
    Player['hand'] = []
    Player['current_bet'] = 0