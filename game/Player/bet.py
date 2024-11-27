def bet(Player, amount):
    """
    Player makes a bet
    :param Player: Player Object
    :param amount: Amount to bet
    :return: True if successful, False otherwise
    """
    if amount <= Player['chips']:
        Player['chips'] -= amount
        Player['current_bet'] += amount
        return True
    return False