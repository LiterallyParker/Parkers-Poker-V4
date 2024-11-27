from .straight import straight
from .flush import flush

def straight_flush(suits: dict, values: list):
    """Returns True if conditions for a four of a kind are met

    Args:
        suits (dict): dictionary of suits from a list of cards, generated by Cards.generate_info
        ranks (list): set of values from a list of cards, generated by Cards.generate_info
    """
    return straight(values) and flush(suits)