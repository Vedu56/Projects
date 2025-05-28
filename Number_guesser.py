import random

random_number = random.randint(1, 100)

def user_guess():

    while True:

        try:
            user_number = int(input("Enter a number between 1 and 100: "))

            if 1 <= user_number <= 100:
                return user_number
            
            else:
                print("Error! Please enter a number between 1 and 100!")

        except ValueError:
            print("Error! Please enter a valid number!")

def check_guess(user_number, random_number):

    if user_number == random_number:
        return "Correct number guessed!"
        
    elif user_number < random_number:
        return "Too low!"

    elif user_number > random_number:
        return "Too high!"
    
def play_game():

    attempts = 0
    won = False

    while attempts < 10:

        attempts += 1
        user_input = user_guess()
        result = check_guess(user_input, random_number)

        if result == "Correct":
            print(f"Congratulations! You have guessed the number {random_number} correctly!")
            won = True
            break

        else:
            print(f"{result} is not correct! Try again!")

    if not won:
        print(f"Sorry! You have ran out of attempts! The number was {random_number}!")

if __name__ == "__main__":
    print("Welcome to the number guessing game!")
    play_game()


        

       
