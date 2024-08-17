import random

def guess_the_number():
    """Function to run the number guessing game."""
    number_to_guess = random.randint(1, 25)
    guessed_correctly = False

    print("Welcome to the Guessing Game!")

    while not guessed_correctly:
        try:
            user_guess = int(input("Guess a number between 1 and 25: "))
            
            if user_guess < 1 or user_guess > 25:
                print("Please enter a number between 1 and 25.")
            elif user_guess < number_to_guess:
                print("Higher!")
            elif user_guess > number_to_guess:
                print("Lower!")
            else:
                print("Congratulations! You've guessed the number!")
                guessed_correctly = True
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()
