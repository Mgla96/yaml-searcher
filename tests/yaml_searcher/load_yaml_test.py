from yamlsearcher.yaml_searcher import load_yaml


def test_dictionary_search_success():
    # arrange
    input = """
    hello: world
    """
    expected = {"hello": "world"}
    # act
    actual = load_yaml(input)
    # assert
    assert actual == expected


def test_dictionary_search_nested_success():
    # arrange
    input = """
    hello: 
      hi:
        hi: world
    """
    expected = {"hello": {"hi": {"hi": "world"}}}
    # act
    actual = load_yaml(input)
    # assert
    assert actual == expected


def test_dictionary_search_arr_success():
    # arrange
    input = """
    hello: 
      - hi: there
        dog: cat
    """
    expected = {"hello": [{"dog": "cat", "hi": "there"}]}
    # act
    actual = load_yaml(input)
    # assert
    assert actual == expected


def test_dictionary_search_empty_val_success():
    # arrange
    input = """
    hello: 
    """
    expected = {"hello": None}
    # act
    actual = load_yaml(input)
    # assert
    assert actual == expected


# TODO: add tests for catching errors
