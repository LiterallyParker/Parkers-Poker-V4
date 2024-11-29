def ordinal_suffix(n):
    """
    Returns the ordinal suffix for a given number (e.g., 'st', 'nd', 'rd', 'th').

    Args:
        n (int): The number to determine the suffix for.

    Returns:
        str: The ordinal suffix ('st', 'nd', 'rd', or 'th').
    """
    if 11 <= n % 100 <= 13:  # Handle 11th, 12th, 13th
        return "th"
    match n % 10:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"