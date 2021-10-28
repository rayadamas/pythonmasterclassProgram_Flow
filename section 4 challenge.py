options = """
1:\tCode
2:\tWatch some anime
3:\tRead some manga
4:\tDo some breathing exercising
5:\tDo 100 push-ups
0:\tquit
"""
print(options)

options2 = ["Code", "Watch some anime", "Read some manga", "Do some breathing exercising", "Do 100 push-ups", "quit"]


chosen_option = "-"

while chosen_option != "0":
    chosen_option = input("Please choose an option: ")
    if chosen_option in "12345":
        print("You chose option {}".format(chosen_option))
    elif chosen_option == "0":
        print("You chose {}".format(chosen_option))
    else:
        print("1:\tCode")
        print("2:\tWatch some anime")
        print("3:\tRead some manga")
        print("4:\tDo some breathing exercising")
        print("5:\tDo 100 pushups")
        print("0:\tquit")
    # chosen_option = input("Please choose an option: ")