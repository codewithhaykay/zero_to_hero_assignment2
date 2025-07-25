###This program calculate the age of a dog in dog years. Where the first two years of a dog's life are equivalent to 10.5 human years each, and every year after that is equivalent to 4 human years.

def calculate_dog_years(n):
    """This function calculates the age of a dog in dog years.
    
    Args:
        n (int): The age of the dog in human years.
    
    Returns:
        int: The equivalent age of the dog in dog years.
    """
    if n < 0:
        return "Age cannot be negative"
    elif n <= 2:
        return n * 10.5
    else:
        return 21 + (n - 2) * 4
    

print(calculate_dog_years(1))
print(calculate_dog_years(6)) 