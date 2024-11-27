from .decode_one import decode_one

def decode_many(nums: list):
    """Decodes a list of card numbers into readable suits and ranks

    Args:
        nums (list): List of card nums

    Returns:
        list: List of cards, ranks and suits
    """
    cards = []
    for num in nums:
        cards.append(decode_one(num))
    return cards