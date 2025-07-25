###This program counts the number of even and odd numbers in a given set.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # a set of numbers to check
# Declare counters for even and odd numbers

even_count = 0  # counter for even numbers

odd_count = 0  # counter for odd numbers  
  
for num in numbers:  # iterate through each number in the set
    
    if num % 2 == 0:  # check if the number is even  
        even_count += 1  # increment the even counter
        
    else:  # if the number is not even, it is odd   
        odd_count += 1  # increment the odd counter
        
        
print(f"The total number of even is: {even_count}")  # print the count of even numbers

print(f"The total number of odd numbers: {odd_count}")  # print the count of odd numbers    