from Dealer import deal

def deal_all(GameState):
    for player in GameState['Players']:
        deal(GameState['Dealer'], player, 2)