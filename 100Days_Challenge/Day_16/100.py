###This program asked for a user full name and returns the Uppercase, Lowercase, 
### TitleCase, Initials, Number of characters without space and number of vowels in the name.
### It also checks if the name is a valid name (only alphabets and spaces allowed).

def creative_full_name():
    full_name = input("Enter your full name: ")

    if not all(x.isalpha() or x.isspace() for x in full_name):
        return "Invalid name. Please enter a valid name."

    uppercase_name = full_name.upper()
    lowercase_name = full_name.lower()
    titlecase_name = full_name.title()
    initials = ''.join([name[0].upper() + '.' for name in full_name.split() if name])
    char_count = len(full_name.replace(" ", ""))
    vowel_count = sum(char in full_name for char in full_name.lower() if char in 'aeiou')

    result = (
        f"Uppercase: {uppercase_name}\n"
        f"Lowercase: {lowercase_name}\n"
        f"TitleCase: {titlecase_name}\n"
        f"Initials: {initials}\n"
        f"Number of characters (without spaces): {char_count}\n"
        f"Number of vowels: {vowel_count}"
    )

    return result


print(creative_full_name())

# # name = "Akeem Lanrewaju Akinyoola"
# # print(len("".join(name.split())))
# # name_gen = sum(nam in name for nam in "".join(name.split()))
# # print(name_gen)
# # print("-".join("Akeem"))

# # print()
# # print("-".join(["Akeem"]))

# greetings = " Hello World \t Python "
# print(" ".join(greetings.split()))

# greetings = "Hello World from Python"
# print("-".join(greetings.split(" ")))

# given_word = "lang=python;level=beginner;days=100"
# print(given_word.split(";")) 
# print() 
# print(given_word.replace("=", ":").split(";"))