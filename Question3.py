###This program prints all even numbers between 1 and 20 inclusive
even_num = []
for x in range(1, 21):
    if x % 2 == 0:
        even_num.append(x)
       
print(f'The requested numbers are: {even_num}')
        