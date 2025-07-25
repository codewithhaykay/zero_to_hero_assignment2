###This program prints the alphabet pattern 'E' using the * symbol
for i in range(7):  # Loop through each row   
    for j in range(6):  # Loop through each column
        if j == 0 or (i == 0 and j < 5) or (i == 3 and j < 4) or (i == 6 and j < 5):
            print('*', end=' ') # Print '*' for the pattern 
        else:
            print(' ', end=' ') # Print space for the rest of the pattern
    print()  # Move to the next line after each row is printed 