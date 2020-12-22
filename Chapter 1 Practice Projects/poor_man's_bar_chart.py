"""Map letters from string into dictionary  and print bar chart of frequency."""
import sys
import pprint
from collections import defaultdict

text = input("Enter a short phrase or sentence: ")

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

mapped = defaultdict(list)
for char in text:
    char = char.lower()
    if char in ALPHABET:
        mapped[char].append(char)

print("\nYou may need to stretch the console window if the tex wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width=110)
