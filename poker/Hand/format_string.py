from Cards import format_string as format_card

def format_string(card_bytes: list):
    string = ""
    for card_byte in card_bytes:
        string += f"{format_card(card_byte):^30}\n"
    return string