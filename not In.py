activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): # converts string to lowercase, AND handles special cases where in other languages, lowered casing changes a words meaning
    print("But I want to go to the cinema!!!")
