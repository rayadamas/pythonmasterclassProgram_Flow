# choice = None
#
# while choice != '0':
#     choice = input("Please enter your choice.  Press enter to quit")
#     if choice == '':
#         break
#
#     print("You have selected {}".format(choice))
# else:
#     print("Thank you for playing, please call back soon.")

# value = 8
# answer = 0
#
# for x in range(1, 13):
#     answer = value * x
#     print("{0} times {1} is {2}".format(x, value, answer))

# taxi = 4
# minibus = 14
# people = 8
#
# if 4 < people <= 14:
#     print("You need a minibus")

# for value in range(11):
#     value *= 2
#     print(value)


choice = None

while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        break

    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")
