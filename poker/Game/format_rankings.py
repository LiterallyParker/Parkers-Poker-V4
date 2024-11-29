from Util import ordinal_suffix
from Global import SCORES
from Hand import format_string as format_hand
def format_rankings(rankings):
    formatted = []
    for rank, (name, score_index, ordered_hand) in enumerate(reversed(rankings), start=1):
        formatted.append(
            f"{rank}{ordinal_suffix(rank)}: {name}\n\n"
            f"{SCORES[score_index].title():^30}\n\n"
            f"{'Hand:':^30}\n{format_hand(ordered_hand)}"
        )
    return "\n".join(formatted)