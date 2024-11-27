from Cards import decode_many

def format_string(Player):
    return (
f"""    Name: {Player['name']}
    Status: {Player['status']}
    Chips: {Player['chips']}
    Hand: {decode_many(Player['hand'])}
    Current Bet: {Player['current_bet']}
"""
    )