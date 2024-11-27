def fold(Player):
    """
    Player folds, resetting their hand and setting status to 'folded'.
    :param Player: Player Object
    """
    Player['status'] = 'folded'
    Player['hand'] = []