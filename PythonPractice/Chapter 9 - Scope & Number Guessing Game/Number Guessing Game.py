import random

attempts = 0
game_on = True


def too_high_or_low(user_guess, answer, attempt):
    if user_guess > answer:
        print("Too high.\nGuess again.")
        return attempt - 1
    elif user_guess < answer:
        print("Too low.\nGuess again.")
        return attempt - 1


def print_guesses(attempt):
    print(f"You have {attempt} remaining to guess the number.")


print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
guess_num = random.randint(1, 100)
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts += 10
        print_guesses(attempts)
        break
    elif difficulty == 'hard':
        attempts += 5
        print_guesses(attempts)
        break
while game_on:
    if attempts == 0:
        game_on = False
        print(f"You have run out of guesses. Answer: {guess_num}. You lose.")
        break

    guess = int(input("Make a guess: "))
    if guess == guess_num:
        game_on = False
        print(f"You got it! The answer was {guess_num}")
    else:
        attempts = too_high_or_low(guess, guess_num, attempts)
        print_guesses(attempts)
