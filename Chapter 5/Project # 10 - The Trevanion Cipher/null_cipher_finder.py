from os import remove
import sys
import string
import load_file


def solve_null_cipher(message, lookahead):
    """Solve a null cipher based on number letters after punctuation mark.
    message = null cipher text as string stripped of whitespace
    lookahead = endpoint of range of letters after punctuation mark to examine
    """
    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print("Using offset of {} after punctuation = {}".format(i, plaintext))
        print()


def main():
    """Load text, solve null cipher."""
    # load & process message:
    filename = input("\nEnter full filename for message to translate: ")
    try:
        loaded_message = load_file.load_text(filename)
    except IOError as e:
        print("{}. Terminating program.".format(e), file=sys.stderr)
        sys.exit(1)
    print("\nORIGINAL MESSAGE =")
    print("{}".format(loaded_message), "\n")
    print("\nList of punctuation marks to check = {}".format(
        string.punctuation), "\n")

    # remove whitespace:
    message = ''.join(loaded_message.split())

    # get rance of possible cipher keys from user:
    while True:
        lookahead = input(
            "\nNumber of letters to check after punctuation mark: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please input a number.", file=sys.stderr)
    print()

    # run function to decode cipher
    solve_null_cipher(message, lookahead)


if __name__ == "__main__":
    main()
