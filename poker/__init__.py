import Cards
import Game.format_rankings
import Game.score_all
import Hand
import Game
import Scoring
import Scoring.format_string
from Global import SCORES

players = [
    {
        "name":"BillyThaKid",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
    {
        "name":"John Travolta",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
    {
        "name":"Amy Schumer",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
    {
        "name":"Micheal Jackson (deceased)",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
]

game_state = {
    "players": players,
    "dealer": {},
    "community_cards":[],
    "pot":0,
    "current_bet":0,
    "round":"pre-flop",
    "allow_bets":False
}


def run_one():
    # Start Game
    Game.start(game_state)

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
    
    # Rank players
    Game.determine_rankings(game_state)
    
    return game_state, [game_state['players'][0]['score_index'], game_state['players'][1]['score_index'], game_state['players'][2]['score_index'], game_state['players'][3]['score_index']]
    
def test_for(score_name):
    # Start Run Timer
    target_score = next((key for key, value in SCORES.items() if value == score_name), None)
    from time import time
    starting = time()
    scores = []
    simulations = 0
    
    while target_score not in scores:
        finished_game, scores = run_one()
        simulations += 1
    print(Game.format_string(finished_game))
    print(Game.format_rankings(finished_game['rankings']))
    ending = time()
    print(f"Runtime: {ending - starting}")
    print(f"Simulations: {simulations}")

while True:
    score_name = input("Test for:\n  ").lower()
    if score_name not in SCORES.values():
        print("Invalid")
        continue
    test_for(score_name)