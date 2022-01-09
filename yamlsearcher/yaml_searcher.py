import os
from sys import stdin, argv, stderr
from yaml import safe_load, dump, YAMLError


def check_search_val(arg_arr):
    if len(arg_arr) <= 1:
        print("supply a value to search for", file=stderr)
        return

    return arg_arr[1]


def dictionary_search(yaml_dict, val):
    split_val = val.split(".")

    for key in split_val:
        yaml_dict = yaml_dict.get(key)
        if yaml_dict is None:
            return
    return yaml_dict


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
    if not isinstance(yaml_input, dict):
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

    yaml_output = dictionary_search(yaml_dict=yaml_input, val=search_val)
    if yaml_output is None:
        return

    if not isinstance(yaml_output, dict):
        yaml_output = dump(yaml_output)

    print(yaml_output)


if __name__ == "__main__":
    main()
