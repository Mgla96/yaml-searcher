"""
This file handles searching through yaml from stdin for a specific value
"""
import os
from sys import stdin, argv, stderr
from typing import List
from yaml import safe_load, dump, YAMLError


def check_search_arg(arg_arr: List[str]) -> str:
    """

    Checks whether arguments were passed to command line
    and returns first argument after name of program

    Parameters
    ----------
    arg_arr
        array of command line arguments

    Returns
    -------
    str
        First argument passed to argv array after name of program
    """
    if len(arg_arr) <= 1:
        print("supply a value to search for", file=stderr)
        return None

    return str(arg_arr[1])


def check_searching_index(val):
    try:
        res = val.split("[")
        if len(res) == 1:
            return res[0], None
        if len(res) == 2:
            return res[0], int(res[1].strip("]"))
    except Exception as err:
        raise err

    raise Exception("failed validating search argument")


def dict_search(yaml_dict: dict, search_field: str) -> dict:
    """Searches through dictionary for the value of a specific field

    Parameters
    ----------
    yaml_dict
        dictionary to search through
    search_field:
        field to search for in dictionary with a '.' as delimiter

    Returns
    -------
    dict
        returns value from yaml_dict with provided search_field

    """
    split_fields = search_field.split(".")

    for key in split_fields:
        key, idx = check_searching_index(key)

        yaml_dict = yaml_dict.get(key)
        if yaml_dict is None:
            return None

        if idx is not None:
            yaml_dict = yaml_dict[idx]

    return yaml_dict


def check_empty_stdin() -> bool:
    """Checks whether anything was provided via stdin

    Returns
    -------
    bool
        whether anything was provided via stdin

    """
    if os.isatty(stdin.fileno()):
        print("empty stdin", file=stderr)
        return True
    return False


def load_yaml(stdin_input: str) -> dict:
    """Loads yaml into dictionary

    Parameters
    ----------
    stdin_input
        yaml input from stdin

    Returns
    -------
    dict
        yaml in dictionary form

    """
    try:
        yaml_input = safe_load(stdin_input)
    except YAMLError as err:
        print(err, file=stderr)
        return None
    if not isinstance(yaml_input, dict):
        return None
    return yaml_input


def format_output(yaml_output):
    """Formats python object to yaml document output format"""
    if isinstance(yaml_output, str):
        return yaml_output

    return dump(yaml_output)


def main():
    """Prints value if it exists from yaml provided on stdin"""

    search_arg = check_search_arg(argv)
    if search_arg is None:
        return

    if check_empty_stdin():
        return

    stdin_data = stdin.read()
    yaml_input = load_yaml(stdin_data)
    if yaml_input is None:
        return

    yaml_output = dict_search(yaml_dict=yaml_input, search_field=search_arg)
    if yaml_output is None:
        return

    print(format_output(yaml_output))


if __name__ == "__main__":
    main()
