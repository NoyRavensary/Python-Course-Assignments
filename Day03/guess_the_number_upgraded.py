import random

def generate_secret_number():
    return random.randint(1, 20)

def play_game():
    while True:
        secret_number = generate_secret_number()
        guesses = 0
        
        while True:
            guess = input("Guess a number between 1 and 20 (or enter 'x' to exit, 'n' to start a new game, or 's' to show the number): ")
            
            if guess.lower() == 'x':
                print("Exiting the game. Goodbye!")
                return
            elif guess.lower() == 'n':
                print("Starting a new game...")
                break
            elif guess.lower() == 's':
                print(f"The secret number is {secret_number}. Shh! Don't tell anyone!")
                continue
            
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 20.")
                continue
            
            guesses += 1
            
            if guess == secret_number:
                print(f"Congratulations! You've guessed the correct number {secret_number}!")
                break
            elif guess < secret_number:
                print("Too small! Try again.")
            else:
                print("Too big! Try again.")
        
        print(f"You needed {guesses} guesses to find the correct number.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Exiting the game. Goodbye!")
            return

def main():
    print("Welcome to the Number Guessing Game!")
    play_game()

if __name__ == "__main__":
    main()
