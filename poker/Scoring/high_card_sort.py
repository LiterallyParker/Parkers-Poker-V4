def high_card_sort(extracted_cards: list, ranks: dict):
    """Returns the card_bits of the high card in an extracted_cards array

    Args:
        extracted_cards (list): dictionary of ranks in a list of cards, generated by Cards.generate_info
    """
    return sorted(
        extracted_cards,
        key = lambda card: (
            ranks[card[2]],
            card[2],
            card[1]
        ),
        reverse=True
    )