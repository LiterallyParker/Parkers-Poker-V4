import Hand
import Game
import Scoring
import Scoring.format_string

players = [
    {
        "name":"BillyThaKid",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
    {
        "name":"JohnMarston",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
    {
        "name":"ColonelSanders",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
    {
        "name":"Parker",
        "chips":500,
        "hand":[],
        "status":"active",
        "current_bet":0,
    },
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

# Start Run Timer
from time import time
starting = time()

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
SCORE0 = Scoring.score(gamestate['players'][0]['hand'] + gamestate['community_cards'])
SCORE1 = Scoring.score(gamestate['players'][1]['hand'] + gamestate['community_cards'])
SCORE2 = Scoring.score(gamestate['players'][2]['hand'] + gamestate['community_cards'])
SCORE3 = Scoring.score(gamestate['players'][3]['hand'] + gamestate['community_cards'])
# Format and print the gamestate and player 1's score
print(Game.format_string(gamestate))
print(f'{"CARDS:":^30}')
print(Hand.format_string(gamestate['players'][3]['hand']))
print(Scoring.format_string(SCORE0))
print(Scoring.format_string(SCORE1))
print(Scoring.format_string(SCORE2))
print(Scoring.format_string(SCORE3))

ending = time()
print("Runtime:", ending - starting)