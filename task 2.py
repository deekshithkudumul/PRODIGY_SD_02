import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print(f"The number is greater than {guess}.")
        elif guess > number_to_guess:
            print(f"The number is less than {guess}.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_the_number()
