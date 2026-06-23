
import random

WORD_LIST = ["python", "hangman", "computer", "keyboard", "diamond"]

MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly select a word from the list."""
    return random.choice(word_list)


def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORD_LIST)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("=" * 40)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord: " + display_progress(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"Congratulations! You guessed the word: {word.upper()}")
            print("=" * 40)
            return

    # Loss condition
    print("\n" + "=" * 40)
    print("Game Over! You ran out of guesses.")
    print(f"The word was: {word.upper()}")
    print("=" * 40)


if __name__ == "__main__":
    play_hangman()

    # Optional replay loop
    while True:
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again == "y":
            play_hangman()
        elif again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'.")
