from .extract_many import extract_many

def count_ranks(card_bytes):
    extracted_cards = extract_many(card_bytes)
    ranks = {}
    for _, rank_bits in extracted_cards:
        if rank_bits not in ranks:
            ranks[rank_bits] = 0
        ranks[rank_bits] += 1
        
    return ranks