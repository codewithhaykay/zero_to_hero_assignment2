###This program accesses a function inside another function and prints the result.

def calculate_square_of_num(num):
    """Function to calculate the square of a number."""
    def square():
        """Inner function to perform the squaring operation."""
        
        return num ** 2
    
    return square()  # Call the inner function to get the square of the number

result = calculate_square_of_num(10)  # Call the outer function with a number

print(f"The square of the number is: {result}")  # Print the result of the calculation
