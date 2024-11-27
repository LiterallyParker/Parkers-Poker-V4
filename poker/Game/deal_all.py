from Dealer import deal

def deal_all(GameState):
    for player in GameState['players']:
        deal(GameState['dealer'], player, 2)