class Room:
    def __init__(self, name, buy_in):
        self.name = name
        self.buy_in = buy_in
        self.players = []
        self.state = 'Idle'
        
    def add_player(self, player):
        if player.chips >= self.buy_in:
            player.chips -= self.buy_in
            self.players.append(player)
            return True
        return False
    
    def start_game(self):
        self.state = 'In Progress'
        return True
    
    def end_game(self):
        self.state = 'Idle'
        return True
    
    def table_info(self):
        return {
            "table_name":self.name,
            "buy_in":self.buy_in,
            "state":self.state
        }