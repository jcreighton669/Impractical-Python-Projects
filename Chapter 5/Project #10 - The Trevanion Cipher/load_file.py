import sys
import string


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
