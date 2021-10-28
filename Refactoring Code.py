# Using the escape Char code
# Refactoring code means changing its structure w/o changing its behavior. May change the HOW, but not the WHAT


# splitStrings
split_string = "This string has been \nsplit over\nseveral\nlines"
print(split_string)

# tabbedString
tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

# Single Quotes
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting"')
# or
# Double Quotes
print("The pet shop owner said \"No, no, \
'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# Line-break with Escape Char
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

# Include Escape Char in String using an additional `\`, or using a RAW string by prefixing the `r` key
print("C:\\Users\\adamasray\\notes.txt")
print(r"C:\Users\adamasray\notes.txt")