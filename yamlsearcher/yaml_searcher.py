from yaml import safe_load, dump, YAMLError
from sys import stdin, argv, stderr
import os


def dictionary_search(d, val):
    split_val = val.split(".")

    for key in split_val:
        d = d.get(key)
        if d is None:
            return None
    return d


def check_empty_stdin():
    if os.isatty(stdin.fileno()):
        print("empty stdin", file=stderr)
        return True
    return False


def main():
    if len(argv) <= 1:
        print("supply a value to search for", file=stderr)
        return

    search_val=argv[1]
    if check_empty_stdin():
        return None

    try:
        yaml_input = safe_load(stdin)
    except YAMLError as err:
        print(err, file=stderr)

    yaml_output = dictionary_search(d=yaml_input, val=search_val)
    print(dump(yaml_output))


if __name__ == "__main__":
    main()
    