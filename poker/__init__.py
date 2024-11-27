from Player import *
from Dealer import *
from Cards import *
from GameState import *

Players = [
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

GameState = {
    "Players": Players,
    "Dealer": {},
    "community_cards":[],
    "pot":0,
    "current_bet":0,
    "round":"pre-flop",
    "allow_bets":False
}

start(GameState)
deal_all(GameState)
flip(GameState, 3)
flip(GameState, 1)
flip(GameState, 1)
cards = GameState['Players'][0]['hand'] + GameState['community_cards']
info = generate_info(cards)
for key, value in info.items():
    print(key, value)