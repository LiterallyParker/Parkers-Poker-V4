from Cards import count_suits, count_ranks, extract_many, extract_rank
from Scoring import high_card, pair, two_pair, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush

def score(player, gamestate):
    """
    Takes in a list of card bytes
    Creates a score int representing the  type (e.g. "Pair", "Two Pair")

    Arguments:
        card_bytes (list): List of card bytes (e.g. [0b100110, 0b001001, ...])

    Returns:
        score (integer): integer representing score
    """
    card_bytes = player['hand'] + gamestate['community_cards']
    # Check for a straight
    flush_result = flush(card_bytes)
    # If both
    if flush_result:
        import Hand
        straight_flush_result = straight(flush_result[:5])
        if straight_flush_result:
            if extract_rank(flush_result[1]) == 13:
                return 9, flush_result
            return 8, flush_result
        return 5, flush_result
    
    four_kind_result = four_of_a_kind(card_bytes)
    if four_kind_result:
        return 7, four_kind_result
    full_house_result = full_house(card_bytes)
    if full_house_result:
        return 6, full_house_result
    straight_result = straight(card_bytes)
    if straight_result:
        return 4, straight_result
    three_kind_result = three_of_a_kind(card_bytes)
    if (three_kind_result):
        return 3, three_kind_result
    two_pair_result = two_pair(card_bytes)
    if (two_pair_result):
        return 2, two_pair_result
    pair_result = pair(card_bytes)
    if pair_result:
        return 1, pair_result

    return 0, high_card(card_bytes)