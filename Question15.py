###This program offers the summation of all numbers in a list.
num_list = [8, 2, 3, 0, 7]  # List of numbers to sum
total_sum = 0  # Variable to hold the sum of numbers
for num in num_list:  # Iterate through each number in the list
    total_sum += num  # Add the current number to the total sum 
print(f"The total sum of the numbers in the list is: {total_sum}") 