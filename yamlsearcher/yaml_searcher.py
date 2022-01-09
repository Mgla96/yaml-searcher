from yaml import safe_load, dump, YAMLError
from sys import stdin, argv, stderr
import os


def check_search_val(arg_arr):
    if len(arg_arr) <= 1:
        print("supply a value to search for", file=stderr)
        return

    return arg_arr[1]


def dictionary_search(d, val):
    split_val = val.split(".")

    for key in split_val:
        d = d.get(key)
        if d is None:
            return
    return d


def check_empty_stdin():
    if os.isatty(stdin.fileno()):
        print("empty stdin", file=stderr)
        return True
    return False


def load_yaml(input):
    try:
        yaml_input = safe_load(input)
    except YAMLError as err:
        print(err, file=stderr)
        return
    return yaml_input


def main():

    search_val = check_search_val(argv)
    if search_val is None:
        return

    if check_empty_stdin():
        return

    yaml_input = load_yaml(stdin)
    if yaml_input is None:
        return

    yaml_output = dictionary_search(d=yaml_input, val=search_val)
    yaml_dump = dump(yaml_output)
    print(yaml_dump)


if __name__ == "__main__":
    main()
