# write a small program to ask for a name & an age
# with both values entered, check if the person is the right age to
# go on an 18-30 holiday (over 18, under 31)

# if they are, welcome them, otherwise print a polite decline


name = input("What is your name? ")
age = int(input("How old are you? "))

if age >= 18 and age <= 31:
    print("Welcome! Enjoy your holiday {}".format(name))
elif age < 18 or age > 30:
    print("Sorry {}, you're outside the required age".format(name))