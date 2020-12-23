"""Turn a word into its Pig LAtin Equivalent."""
import sys

VOWELS = 'aeiouy'

while True:
    word = input("Type a word and getits pig lating translation: ")
    pig_latin_word = ''
    if word[0] in VOWELS:
        pig_latin_word = word + "way"
    else:
        pig_latin_word = word[1:] + word[0] + "ay"

    print("\n{}".format(pig_latin_word), file=sys.stderr)

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
    if try_again.lower() == "n":
        break


input("\nPress Enter to exit.")
