parrot = "Norwegian Blue"

for character in parrot:
    print(character)

# Challenge
# Write a program to print out the capital letters in a string
# Check out the string methods for one way to test if a character is in uppercase

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
print()
# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)