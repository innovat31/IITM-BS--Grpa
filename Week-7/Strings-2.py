# Actual Solution :

def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    
    
    mid = len(s) // 2
    return 'a' in s[mid:] or 'A' in s[mid:]
    # alternate way
    # return 'a' in s[mid:].lower()d
    
# My Solution :

def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    half_length = len(s) // 2
    second_half = s[half_length:]
    return 'a' in second_half.lower()

