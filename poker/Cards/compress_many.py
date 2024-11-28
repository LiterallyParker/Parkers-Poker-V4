from .compress_one import compress_one

def compress_many(extracted_cards):
    return [compress_one(card) for card in extracted_cards]