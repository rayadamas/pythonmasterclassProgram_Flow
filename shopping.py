shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)
# Break causes the code to be terminated once that line is reached

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# Using Continue: causes all remaining code in a block to be skipped
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

