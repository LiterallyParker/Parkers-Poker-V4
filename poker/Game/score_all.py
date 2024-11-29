from Scoring import score

def score_all(game_state):
    for player in game_state['players']:
        score_index, ordered_hand = score(player, game_state)
        player['score_index'] = score_index
        player['ordered_hand'] = ordered_hand