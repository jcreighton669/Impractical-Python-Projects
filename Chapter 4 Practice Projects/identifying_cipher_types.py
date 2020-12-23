from os import sep
import sys
import load_dictionary
from collections import Counter

CUTOFF = 0.5

try:
    ciphertext_a = load_dictionary.load(
        'Chapter 4 Practice Projects\cipher_a.txt')


except IOError as e:
    print("{}. Terminating program.".format(e), file=sys.stderr)
    sys.exit(1)

try:
    ciphertext_b = load_dictionary.load(
        'Chapter 4 Practice Projects\cipher_b.txt')

except IOError as e:
    print("{}. Terminating program.".format(e), file=sys.stderr)
    sys.exit(1)

# count 6 most-common letters in ciphertext
six_most_frequent = Counter(ciphertext_a.lower()).most_common(6)
print("\nSix most-frequently-used letters in English = ETAOIN")
print("\nSix most frequent letters in ciphertext =")
print(*six_most_frequent, sep='\n')

cipher_top_six = {i[0] for i in six_most_frequent}

TARGET = 'etaoin'
count = 0
for letter in TARGET:
    if letter in cipher_top_six:
        count += 1

if count / len(TARGET) >= CUTOFF:
    print("\nThis ciphertext is most-likely produced by a TRANSPOSITION cipher")
else:
    print("This ciphertext is most-likely produced by a SUBSTITUTION cipher")

six_most_frequent = Counter(ciphertext_b.lower()).most_common(6)
print("\nSix most-frequently-used letters in English = ETAOIN")
print("\nSix most frequent letters in ciphertext =")
print(*six_most_frequent, sep='\n')

cipher_top_six = {i[0] for i in six_most_frequent}

TARGET = 'etaoin'
count = 0
for letter in TARGET:
    if letter in cipher_top_six:
        count += 1

if count / len(TARGET) >= CUTOFF:
    print("\nThis ciphertext is most-likely produced by a TRANSPOSITION cipher")
else:
    print("This ciphertext is most-likely produced by a SUBSTITUTION cipher")
