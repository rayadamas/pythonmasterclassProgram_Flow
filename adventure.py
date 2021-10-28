available_exits = ["north", "south", "east", "west"]

# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#
# print("Aren't you glad you got out of there?!")

# Break example

# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game over man")
#         break
#
# else:
#     print("Aren't you glad you got out of there?!")

# Code Exercise 10
# Modify the code inside this loop to stop when i is exactly divisible by 11
# That number should be the last value printed
# Code should print the same values as it currently does, but stop after printing a number divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
#         print(i)

# Coding Exercise 11
# Write out a program to print out all the numbers from 0 - 20 that aren't divisible by 3 or 5
# 0 is divisible by everything (0 should not be in the output)
for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)