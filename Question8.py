###This program prompt a user for a word and then prints the word in reverse order.
word = input("Enter a word: ")  # prompt the user for a word

reversed_word = ""  # an empty string to collect the reversed word
for char in word:  # iterate through each character in the word
    reversed_word = char + reversed_word  # prefix the character in the given word to the reversed word          
    
print(f"The reversed word is: {reversed_word}")


