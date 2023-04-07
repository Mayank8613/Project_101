import random

user = (input("Do you want to roll a dice?"))
response = "y"
while (response == "y"):
    no = random.randint(1,6)
    if user.on:
        #make the dice
        if response == "n":
            print("GAME OVER")
