# Actual Solution :

def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
    Arguments:
    n1: int - the first number
    n2: int - the second number

    Return:
    int - the number of unique common digits.
    '''
    
    return len(set(str(n1)) & set(str(n2)))


# My Solution :

def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3

    Arguments:
    n1: int - the first number
    n2: int - the second number

    Return:
    int - the number of unique common digits.
    '''
    # Convert the numbers to sets of digits
    digits_n1 = set(str(n1))
    digits_n2 = set(str(n2))
    
    # Find the intersection of both sets and return its length
    common_digits = digits_n1.intersection(digits_n2)
    return len(common_digits)
