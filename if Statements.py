name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))
# using `int`, a value that actually IS an `int` must be input
print(age)

if age >= 18:
    print("You're old enough to vote!")
    print("Please put an X in the box.")
else:
    print("Please come back in {0} years when you're old enough to vote here in Aussie Land!".format(18 - age))

if age < 18:
    print("Please come back in {0} years when you're old enough to vote here in Aussie Land!".format(18 - age))
else:
    print("You're old enough to vote!")
    print("Please put an X in the box.")
