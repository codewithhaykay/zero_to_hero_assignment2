###This program demonstrates how a function is used to accept two integers as arguments and sum the two integers together.But, if the sum is bween 15 and 20, it returns 20 instead of the actual sum.

def add_two_integers(x, y):
    """This function takes two integers and returns their sum.
    
    Args:
        x (int): The first integer.
        y (int): The second integer.
    
    Returns:
        int: The sum of the two integers, or 20 if the sum is between 15 and 20.
    """
    total = x + y
    if 15 < total < 20:
        return 20
    return total

print(add_two_integers(10, 6)) 
print(add_two_integers(10, 8))   