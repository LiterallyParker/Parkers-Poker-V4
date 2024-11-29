def determine_rankings(game_state):
    all_hands = []
    
    # Iterate over players
    for player in game_state['players']:
        # If player is still in
        if player['status'] != 'folded':
            # Add their cards to the comparison array
            all_hands.append((player['name'], player['score_index'], player['ordered_hand']))
            
    print("\nInitial Hands for All Players:")
    for hand in all_hands:
        print(hand)
        
    # Player sorting key
    def compare_scores(player_score_info):
        score_index = player_score_info[1]
        ordered_hand = player_score_info[2]
        
        card_values = [
            (card & 0b1111, card >> 4) for card in ordered_hand
        ]
        print(f"\nPlayer: {player_score_info[0]}, Score: {player_score_info[1]}, Hand: {card_values}")
        
        return (
            -score_index,
            [-((card & 0b1111) + ((card >> 4) * 0.01)) for card in ordered_hand]
        )
    
    game_state['rankings'] = sorted(all_hands, key=compare_scores, reverse=True)
    
    print("\nPost Sort:")
    for ranking in game_state['rankings']:
        print(ranking)
    
    return game_state