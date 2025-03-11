import random


def print_state(word_, lives_, letters_):
    for ch in word_:
        if ch in letters_:
            print(ch, end="")
        else:
            print("_", end="")
    print("\n")
    print(f"Lives remaining: {lives_}")
    print(f"Letters guessed: {letters_}")


def is_complete(word_, letters_):
    for ch in word_:
        if ch not in letters_:
            return False
    return True


lives = 6
words = ["mouse", "crab", "hat", "fridge"]

word = random.choice(words).upper()
letters_guessed = []

while lives:
    print_state(word, lives, letters_guessed)
    letter = input("Please, guess a letter: ").upper()
    if letter in letters_guessed:
        print(f"You already guessed '{letter}'.")
        lives -= 1
        continue
    letters_guessed.append(letter)
    # letters_guessed.sort()
    if letter in word:
        if is_complete(word, letters_guessed):
            print_state(word, lives, letters_guessed)
            print(f"Congratulations! You won! The word was {word}")
            break
        continue
    lives -= 1
else:
    print(f"Unfortunately, you ran out of lives, so you lost the game. The word was {word}.")
