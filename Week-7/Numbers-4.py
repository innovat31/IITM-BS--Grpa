# Actual solution

def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    '''
    Given three side lengths in the increasing 
    order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right 
    triangle whose perpendicular sides are of even length.

    Hint: in a right triangle the square of hypotenuse is the sum of square of other two sides.

    Arguments:
    a: int - the first side length
    b: int - the second side length
    c: int - the hypotenuse length

    Return:
    bool - True if the sides form a right triangle and the perpendicular sides are even, else False
    '''
    
    return a**2 + b**2 == c**2 and a % 2 == 0 and b % 2 == 0

# My solution

def is_right_triangle_with_even_sides(a: int, b: int, c: int) -> bool:
    '''
    Given three side lengths in the increasing 
    order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right 
    triangle whose perpendicular sides are of even length.

    Hint: in a right triangle the square of hypotenuse is the sum of square of other two sides.

    Arguments:
    a: int - the first side length
    b: int - the second side length
    c: int - the hypotenuse length

    Return:
    bool - True if the sides form a right triangle and the perpendicular sides are even, else False
    '''
    # Check if it's a right triangle using Pythagorean theorem
    if a**2 + b**2 == c**2:
        # Check if the perpendicular sides are even
        if a % 2 == 0 and b % 2 == 0:
            return True
    return False
