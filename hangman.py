import random

words = ["apple", "tiger", "chair", "robot", "pizza"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("Correct Guess!")
        else:
            print("You already guessed that letter.")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)