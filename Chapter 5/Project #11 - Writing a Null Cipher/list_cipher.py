from random import randint
import string
import load_file

# write a short message that doesn't contain punctuation or numbers!
input_message = "Panel at east end of chapel slides"

message = ''
for char in input_message:
    if char in string.ascii_letters:
        message += char
print(message, "\n")
message = "".join(message.split())

# Open dictionary file
word_list = load_file.load_dict('2of4brif.txt')

# Build vocabulary word list with hidden message
vocab_list = []
for letter in message:
    size = randint(6, 10)
    for word in word_list:
        if len(word) == size and word[2].lower() == letter.lower() and word not in vocab_list:
            vocab_list.append(word)
            break

if len(vocab_list) < len(message):
    print("Word list is too small. Try larger dictionary or shorter message!")
else:
    print("Vocabulary words for Unit 1: \n", *vocab_list, sep="\n")
