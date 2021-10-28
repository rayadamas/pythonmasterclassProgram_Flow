age = int(input("How old are you? "))


# Using `and`, BOTH parts of the statement must are evaluated to be True
# Using `or`, one OR the other option could be True

#if age >= 16 and age <= 65:
# if 16 <= age <= 65:
if age in range(16,66):
    print("Have a good day at work!")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work!")



