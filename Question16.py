###This program checks if a number is prime or not using a function declaration.

def is_prime_num(n):
    """Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        statement: if the number is prime or otherwise.
    """
    if n < 2: #this checks if n is either 0 or 1
        return f'{n} is not a prime number'
    else:
        is_prime = True # Assume n is prime until proven otherwise
        
        # Check for factors from 2 to n-1 and if n is divisible by any of them, it is not a prime number.
        for i in range(2, n):
            if n % i == 0:
                is_prime = False # if n is divisible by any number other than 1 and itself, it is not prime
                
                break # exit the loop early if a factor is found
            
        if is_prime: # if no factors were found, n is a prime number
            
            return f'{n} is a prime number'
        else:
            return f'{n} is not a prime number'
        
###Test the function with different numbers
print(is_prime_num(2))
print(is_prime_num(21)) 