import random

dice = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six"
}

while True:

    userChoice = input("Do you want to roll the dice? [Y/N]: ").upper()
    
    if userChoice == "Y":
        
        diceOutput = random.randint(1,6)
        diceResult = dice[diceOutput]
        
        print(f"You rolled a {diceOutput}!")

        break

    elif userChoice == "N":
        print("Exiting program....")
        break

    else:
        print("Error! Please enter N or Y!")

    