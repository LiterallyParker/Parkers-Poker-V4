def compress_one(extracted_card):
    """
    Compresses previously extracted card back into bytes
        byte format:
        rank/suit
        4b/2b

    Args:
        extracted_card (tuple): a tuple containing a rank index and a suit index 

    Returns:
        list: compressed cards

    """
    return (extracted_card[0] << 2) | extracted_card[1]