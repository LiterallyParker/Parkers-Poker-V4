import Player
import Dealer
import Cards
import Scoring
import Game

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

from time import time
starting = time()

Game.start(gamestate)
Game.deal_all(gamestate)
Game.flip(gamestate, 3)
Game.flip(gamestate, 1)
Game.flip(gamestate, 1)
SCORE = Player.score(gamestate['players'][0], gamestate['community_cards'])

print(Game.format_string(gamestate))
print(SCORE)

ending = time()
print("Runtime:", ending - starting)