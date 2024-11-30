import Player
from Hand import format_string as format_hand
def format_string(game_state):
    # formatted_players = "\n".join(format_player(player) for player in game_state['players'])
    GAME_STRING = f"""\n{"PARKER'S POKER":_^30}\n"""
    
    # Stringify Players
    player_strings = []
    for player in game_state['players']:
        player_string = Player.format_string(player)
        player_strings.append(player_string)
    
    players_string = "".join(player_strings)
    GAME_STRING += players_string
    
    # Stringify Community
    community_string = f"""\n{"COMMUNITY CARDS":_^30}\n"""
    community_string += format_hand(game_state['community_cards'])
    GAME_STRING += community_string + "\n"
    
    # Stringify Winner
    winner_string = f"""\n{"WINNER":_^30}"""
    GAME_STRING += f"{winner_string}\n\n{Player.format_string(game_state['winner'])}"
    return GAME_STRING

"""Absolutely! Here are a few details that could improve coding help:

    Preferred Programming Languages: Knowing which languages you work with most (e.g., Python, JavaScript, etc.).
    
    Development Focus: Your main areas of interest (e.g., web development, mobile apps, machine learning, game development).
    
    Tools/Frameworks: Specific frameworks, libraries, or tools you use (e.g., React, Django, Docker).
    
    Workflow: Your preferred version control tools, IDEs, or methodologies (e.g., Git, Agile).
    Experience Level: Whether you’re more comfortable with beginner, intermediate, or advanced coding concepts.
    
    Common Challenges: Types of issues you encounter often (e.g., debugging, optimization, architecture design).
    
    Coding Style: If you follow specific paradigms like OOP, functional programming, or a mix.
    Learning Goals: Skills or technologies you want to focus on improving.
    
Would you like to share anything from the above list? It’ll help me tailor advice more effectively!"""