from Card import extract_rank
from Scoring import high_card, pair, two_pair, three_of_a_kind, straight, flush, full_house, four_of_a_kind

def score(player, game_state):
    """
    Creates a score tuple for a given player

    Arguments:
        player (dict): Player dictionary containing:
            - player['name'] (str)
            - player['chips'] (int)
            - player['hand'] (list): list of player card bytes
            - player['status'] (str)
            - player['current_bet'] (int)
        game_state (dict): Game state dictionary, containing community_cards, players, etc

    Returns:
        score (tuple): tuple containing:
            - score[0] (int): The numeric score index (Global.SCORES)
            - score[1] (list): Ordered list of card bytes, by relevancy
    """
    # Combine card bytes
    card_bytes = player['hand'] + game_state['community_cards']

    flush_result = flush(card_bytes)

    if flush_result:
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