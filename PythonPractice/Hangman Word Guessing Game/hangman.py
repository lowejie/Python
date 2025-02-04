import random

# Introduction
print("Welcome to Hangman!")

# Word list and initialization
words = ["apple", "orange", "lemon"]
guess_word = random.choice(words)
guess_word_list = list(guess_word)
blank_word = ["_"] * len(guess_word)
print("The word to guess:", " ".join(blank_word))

# Game variables
game_on = True
lives = 6
guessed_letters =[]

# Game loop
while game_on:
    print("\n" + " ".join(blank_word))  # Display the current state of the word
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ").lower()


    # Check if the guessed letter is in the word
    if guess in guessed_letters:
        print("already guessed. try again.")
    elif guess in guess_word_list:
        for index, letter in enumerate(guess_word_list):
            if letter == guess:
                blank_word[index] = guess
        print(f"Good guess! {guess} is in the word.")
        guessed_letters.append(guess)
    else:
        print(f"Guessed {guess}, wrong. Lose a life.")
        guessed_letters.append(guess)
        lives -= 1

    # Check for win or lose conditions
    if "_" not in blank_word:
        game_on = False
        print("\nCongratulations! You guessed the word:", "".join(blank_word))
    elif lives == 0:
        game_on = False
        print("\nGame over! The word was:", guess_word)
