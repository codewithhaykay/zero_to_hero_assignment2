### This python program construct a given pattern using the * symbol

#The outer for loop goes through interate through the symbols just once.

for i in range(1, 2):
    
    #The first inner loop ensure the increment of the symbols up to 5 in a row
    
    for k in range(1, 6):
        print('*' * k)
        
        #The second inner loop ensures the decrement of the symbol down to 1 from 4 in a row.
        
    for k in range(4, 0, -1):
        print('*' * k)