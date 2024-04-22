import random

print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 20)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    guesses += 1
    
    if guess == secret_number:
        print(f"Congratulations! You've guessed the correct number {secret_number}!")
        break
    elif guess < secret_number:
        print("Too small! Try again.")
    else:
        print("Too big! Try again.")

print(f"You needed {guesses} guesses to find the correct number.")
