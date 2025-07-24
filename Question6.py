###This program prints all numbers except 3 and 6
for y in range(7): #This loop through the available numbers
    if y in (3, 6):
        continue   # the continue statement ensures that both 3 and 6 skipped
    print(y, end=' ')  #The end keyword is simply to layout the output horizontally.