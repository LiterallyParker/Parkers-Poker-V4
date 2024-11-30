from Card import format_string as format_card

def format_string(card_bytes: list):
    strings = [f"{'-'*20:^30}"]
    for card_byte in card_bytes:
        strings.append(f'{format_card(card_byte):^30}')
    strings.append(f"{'-'*20:^30}")
    return "\n".join(strings)