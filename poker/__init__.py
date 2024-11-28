import Cards
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
    }
]

gamestate = {
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
    Game.start(gamestate)

    # Deal to players
    Game.deal_all(gamestate)

    # Flop
    Game.flip(gamestate, 3)

    # Turn
    Game.flip(gamestate, 1)

    # River
    Game.flip(gamestate, 1)
    
    return (Scoring.score(gamestate['players'][0], gamestate))
    
def test_for(score_name):
    # Start Run Timer
    target_score = next((key for key, value in SCORES.items() if value == score_name), None)
    from time import time
    starting = time()
    score = run_one()
    while not score[0] == target_score:
        score = run_one()
    print(Game.format_string(gamestate))
    print(Scoring.format_string(score))
    ending = time()
    print("Runtime:", ending - starting)
    
test_for("Straight")