import random

words = ["pen", "pencil", "ruler", "rubber", "sharpner", "calculator", "notebook"]

random_word = random.choice(words)

print("Welcome! Try to guess the correct word! \nHINT: It's stationary!")

turns = 10
guesses = " "

def guess():
    global turns, guesses

    while turns > 0:

        failed = 0
        display = ""

        for char in random_word:

            if char in guesses:
                display += char

            else:
                print("_")
                failed += 1

        print("Word: ", "".join(display))

        if failed == 0:
            print(f"Congrats! You've correctly guessed the word! \nWord was {random_word}!")
            break

        try:
            user_guess = input("Enter a character of the word: ").lower()

            if len(user_guess) != 1 or not user_guess.isalpha():
                raise ValueError
            
            if user_guess in guesses:
                print("You've already guessed that character!")
                continue

            guesses += user_guess

            if user_guess not in random_word:
                turns -= 1
                print(f"Incorrect! You have {turns} guesses left!")

            if turns == 0:
                print(f"You lose! The correct word was {random_word}!")
                break

        except ValueError:
            print("Error! Please enter a character!")

guess()

            


