def determine_winner(game_state):
    all_hands = []
    
    # Iterate over players
    for player in game_state['players']:
        # If player is still in
        if player['status'] != 'folded':
            # Add their cards to the comparison array
            all_hands.append((player, player['score_index'], player['ordered_hand']))
        
    # Player sorting key
    def compare_scores(player_score_info):
        score_index = player_score_info[1]
        ordered_hand = player_score_info[2]
        
        card_values = [
            ((card >> 2), (card & 0b11)) for card in ordered_hand
        ]
        
        return (
            -score_index,
            [-((card >> 2) + ((card & 0b11) * 0.01)) for card in ordered_hand]
        )
    
    ranked_hands = sorted(all_hands, key=compare_scores)
    game_state['winner'] = ranked_hands[0][0]

    return game_state