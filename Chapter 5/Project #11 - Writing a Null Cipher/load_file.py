"""Load a text file as a list.

Arguments: 
-text file name (and directory path, if needed)

Exceptions:
-IOError if filename not found.

Returns: 
-A list of all words in a text file in lower case.

Requires-import sys

"""
import sys


def load_dict(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(
            e, file), file=sys.stderr)
        sys.exit(1)


def load_text(file):
    """Open text file and return list."""
    with open(file) as f:
        return f.read().strip()
