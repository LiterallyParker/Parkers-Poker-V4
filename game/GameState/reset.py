def reset(GameState):
    GameState['community_cards'] = []
    GameState['pot'] = 0
    GameState['current_bet'] = 0
    GameState['allow_betting'] = False,
    GameState['round'] = 'pre-flop'