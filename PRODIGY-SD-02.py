import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guessing_game()
