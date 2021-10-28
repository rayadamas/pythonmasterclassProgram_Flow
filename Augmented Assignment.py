# x = 23
#
# x += 1
# print(x) # 24
#
# x -= 4
# print(x) # 20
#
# x *= 5
# print(x) # 100
#
# x //= 4
# print(x) # 25
#
# x /= 5
# print(x) # 5.0 - note the conversion from an int to a float
#
# x **= 2
# print(x) # 25.0
#
# x %= 5
# print(x) # 0.0 - 25 is exactly divisible by 5
#
# greeting = "Good"
#
# greeting += " morning. "
# print(greeting)
#
# greeting *= 5
# print(greeting)

# Coding Exercise 12
# Use a For loop & augmented assignment to give ANSWER the result of multiplying NUMBER by MULTIPLIER

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for x in range(multiplier):
    answer += number

print(answer)
