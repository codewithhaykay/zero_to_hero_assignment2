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

