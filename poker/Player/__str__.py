from output_string import output_string

def __str__(Player):
    return f"\n{Player['name']:^30}\n{f'({Player['status']})':^30}\n{output_string('Chips', Player['chips'])}\n{output_string('Bet', Player['current_bet'])}\n"