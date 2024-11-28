from .straight_flush import straight_flush

def royal_flush(suits: dict, values: list):
    """
    Returns True if conditions for a royal flush are met

    Args:
        suits (dict): dictionary of suits
        ranks (dict): dictionary of ranks
    """
    return straight_flush(suits, values) and 14 in values