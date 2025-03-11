# nato_alphabet = {
#     "a": "alpha",
#     "b": "bravo",
#     "c": "charlie",
#     "d": "delta",
#     "e": "echo",
#     "f": "foxtrott",
#     "g": "golf",
#     "h": "hotel",
#     "i": "india",
#     "j": "juliet",
#     "k": "kilo",
#     "l": "lima",
#     "m": "mike",
#     "n": "november",
#     "o": "oscar",
#     "p": "papa",
#     "q": "quebec",
#     "r": "romeo",
#     "s": "sierra",
#     "t": "tango",
#     "u": "uniform",
#     "v": "victor",
#     "w": "whiskey",
#     "x": "x-ray",
#     "y": "yankee",
#     "z": "zulu"}
import pandas as pd
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv", delimiter=",")

# nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
nato_alphabet_dict = dict(zip(nato_alphabet.letter, nato_alphabet.code))

# Modified on Day 30 to handle exceptions
is_input_valid = False
while not is_input_valid:
    try:
        entered = input("Type a string which you want to spell: ")
        print([nato_alphabet_dict[letter] for letter in entered.upper()])
    except KeyError:
        print("Sorry, letters only.")
    else:
        is_input_valid = True


