###This program is designed to calculate the fibonacci series of numbers between 0 and 50
###the fibonacci number is a number that is the sum of the two preceeding number in a series.

def fibonacci_of_num(n):
    """The program return the fibonacci series of any number.

    Args:
        n (int): takes in the value of any number to be determined in the series

    Returns:
        int: return the base cases together with the intended number whose fibonacci is to be determined.
    """
    if n <= 1:  
        return n # return the base case (0 and 1)
    else:
        return fibonacci_of_num(n -1) + fibonacci_of_num(n -2)    #keeps the sequence rolling until the base case is reached.
    
for x in range(11):
    print(fibonacci_of_num(x), end=" ")