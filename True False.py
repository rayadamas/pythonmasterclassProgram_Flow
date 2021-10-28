day = "Monday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) and not raining:
    print("Go swimming")
else:
    print("Learn python")



# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learn python")




if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")