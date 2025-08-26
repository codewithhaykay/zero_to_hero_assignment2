###This program request a user for numbers and quit upon getting zero. It goes ahead to add all the values it got together.

quit = 0
total = 0  # the total is to collect and calculate the numbers
collected_num = [] #this list is used for collecting the numbers entered by the user.

while collected_num != quit:
    num = int(input("Enter a number or 0 to quit: "))
    if num == quit:
        break
    if num != quit:
        collected_num.append(num) #This ensures that the empty list is filled with the numbers as they are being collected.
        
#The for loop here help sum up the collected numbers
for x in collected_num:
    total = total + x
    
print("The total of the numbers collected is: ", total)


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


###This program accesses a function inside another function and prints the result.

def calculate_square_of_num(num):
    """Function to calculate the square of a number."""
    def square():
        """Inner function to perform the squaring operation."""
        
        return num ** 2
    
    return square()  # Call the inner function to get the square of the number

result = calculate_square_of_num(10)  # Call the outer function with a number

print(f"The square of the number is: {result}")  # Print the result of the calculation
