from .compress_one import compress_one

def compress_many(extracted_cards: list):
    """
    Compresses previously extracted cards back into bytes
        byte format:
        rank/suit
        4b/2b

    Args:
        extracted_cards (list): list of tuples containing a suit index and a rank index

    Returns:
        list: compressed cards

    """
    return [compress_one(card) for card in extracted_cards]