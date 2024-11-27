from .decode_one import decode_one

def decode_many(nums):
    suitRanks = []
    for num in nums:
        suitRanks.append(decode_one(num))
    return suitRanks