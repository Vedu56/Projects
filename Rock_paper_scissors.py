import random

user_options = {
    1: "rock",
    2: "paper",
    3: "scissor"
}

def determine_winner(computer, user):

    if computer == user:
        return "Draw!"
    elif (computer == 2 and user == 3) or (computer == 3 and user == 1) or (computer == 1 and user == 2):
        return "User won!"
    else:
        return "Computer won!"
    
while True:

    print("Rock => 1 \nPaper => 2 \nScissors => 3")

    try: 
        user_choice = int(input("Enter your choice: "))

        if user_choice not in user_options:
            print("Error! Please enter a valid choice!")
            
            
    except ValueError:
        print("Error! Please enter a number from the options above!")
        continue

    user_choice1 = user_options[user_choice]
    print(f"The User's choice is {user_choice1}!")

    computer_choice = random.randint(1,3)
    computer_choice1 = user_options[computer_choice]
    print(f"The Computer's choice is {computer_choice1}!")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "Draw!":
        print("Tie!")
        break
    elif winner == "Computer won!":
        print("Computer wins!")
        break
    else:
        print("User wins!")
        break
        

