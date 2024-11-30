import Game

def run_one():
    
    players = [
        {
            "id":0,
            "name":"BillyThaKid",
            "chips":500,
            "hand":[],
            "status":"active",
            "current_bet":0,
            "score_index":0
        },
        {
            "id":1,
            "name":"John Travolta",
            "chips":500,
            "hand":[],
            "status":"active",
            "current_bet":0,
            "score_index":0
        },
        {
            "id":2,
            "name":"Amy Schumer",
            "chips":500,
            "hand":[],
            "status":"active",
            "current_bet":0,
            "score_index":0
        }
    ]
    
    game_state = {
        "players": players,
        "dealer": {},
        "community_cards":[],
        "pot":0,
        "current_bet":0,
        "round":"pre-flop",
        "allow_bets":False,
        "winner":None
    }
    
    # Start Game
    Game.start(game_state)
    print(f'{"STARTING":^30}')
    print(game_state)
    # Deal to players
    Game.deal_all(game_state)

    # Flop
    Game.flip(game_state, 3)

    # Turn
    Game.flip(game_state, 1)

    # River
    Game.flip(game_state, 1)
    
    # Scoring
    Game.score_all(game_state)
    
    # Determine Winner
    Game.determine_winner(game_state)
    
    return game_state

def test():
    finished_game = run_one()
    print(Game.format_string(finished_game))

test()