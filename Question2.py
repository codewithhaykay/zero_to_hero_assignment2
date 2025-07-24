###This program prints numbers in descending order from 10 to 1

num_in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # provides the list of numbers

new_numlist = []  # an empty list for collecting the sorted numbers in descending order

while num_in_list:
    largest = num_in_list[0]
    for i in num_in_list:
        if i > largest:
            largest = i
            
    new_numlist.append(largest)
    num_in_list.remove(largest)
    
#The for loop output the numbers in the required format

for descend_num in new_numlist:
    print(descend_num)
            