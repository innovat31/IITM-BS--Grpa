# Actual Solution

def common_char_sorted_str(s1:str, s2:str) -> str: 
    '''Returns a sorted string with unique common charecters present in the given strings.

    Arg:
        s1 (str) : Input string. 
        s2 (str) : Input string. 

    Returns: 
        str: string of unique common charecters arranged in ascending order. 

    Examples:
    >>> common_char_sorted_str('apple', 'ball')
    'al'
    >>> common_char_sorted_str('abcde', 'edfci')
    'cde'
    '''
    
    return ''.join(sorted(set(s1) & set(s2)))

# My Solution

def common_char_sorted_str(s1:str, s2:str) -> str:  
    '''Returns a sorted string with unique common charecters present in the given strings. 
    Arg: 
        s1 (str) : Input string.  
        s2 (str) : Input string.  
    Returns:  
        str: string of unique common charecters arranged in ascending order.  
    Examples: 
    >>> common_char_sorted_str('apple', 'ball') 
    'al' 
    >>> common_char_sorted_str('abcde', 'edfci') 
    'cde' 
    ''' 
     # Convert strings to sets and find the intersection 
    common_chars = set(s1).intersection(set(s2)) 
    # Sort the common characters 
    sorted_common_chars = sorted(common_chars) 
# Join the sorted common characters into a string 
    return ''.join(sorted_common_chars)
