# 1st method (Original solution)

def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.


    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list
    '''
    
    
    n = len(lst)
    k = k % n
    return lst[n-k:] + lst[:n-k]
    
# 2nd method (My solution)

def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.

    Arguments:
        lst (list): a list of items
        k (int): the number of steps to rotate the list to the right

    Returns:
        list: the rotated list

    Example:
    >>> rotate_list([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    '''
    n = len(lst)
    effective_k = k % n
    return lst[-effective_k:] + lst[:-effective_k]
