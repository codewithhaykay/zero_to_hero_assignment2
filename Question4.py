###This program uses while loop to print the odd numbers between 1 and 15 inclusively.

done = range(1, 16) #The range function is used to generate a list of numbers between 1 and 15 inclusively.

while done: 
    for y in done:
        if y % 2 == 1: #This line ensures that the numbers when divided by 2 leaves a remainder of 1
            
            print(y, end=" ")
            
    done = False
    