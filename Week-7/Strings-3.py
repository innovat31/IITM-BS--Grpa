
def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    
    
    first_letter_counts = {}
    for word in passage.lower().split(): 
        first_letter = word[0]
        if first_letter not in first_letter_counts:
            first_letter_counts[first_letter] = 0
        first_letter_counts[first_letter] += 1

    return max(first_letter_counts, key=first_letter_counts.get)
    
# My solution :

def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word (case insensitive).

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    from collections import Counter
    words = passage.split()
    first_letters = [word[0].lower() for word in words if word]  # Get first letter of each word
    most_common = Counter(first_letters).most_common(1)
    return most_common[0][0] if most_common else ''

