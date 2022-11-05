print("This is a flowchart of discovery questions for Suit Supply")

print("1. Wedding\t2. First Suit\t3.Business\t4.Luxury")
userOccasion = int(input("What occasion were you shopping for? "))

if (userOccasion == 1):  # Wedding
    print("Is the wedding indoor or outdoor?\n")
    print("Is there a theme or dress code?\n")
    print("What is the look that you're going for?\n")
elif (userOccasion == 2):  # First Suit
    print("")
elif (userOccasion == 3):  # Business
    print("What sector do you work in?\n")
    print("How often do you wear a suit?\n")
    print("How many suits do you own?\n")
    print("What color suits do you already have?\n")
elif (userOccasion == 4):  # Luxury
    print("")

