from yamlsearcher.yaml_searcher import load_yaml


def test_load_yaml_success():
    # arrange
    input = """
    hello: world
    """
    expected = {"hello": "world"}
    # act
    actual = load_yaml(input)
    # assert
    assert actual == expected


def test_load_yaml_nested_success():
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


def test_load_yaml_arr_success():
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


def test_load_yaml_empty_val_success():
    # arrange
    input = """
    hello: 
    """
    expected = {"hello": None}
    # act
    actual = load_yaml(input)
    # assert
    assert actual == expected


def test_load_yaml_invalid_dict_failure():
    # arrange
    input = "hello"
    expected = None
    # act
    actual = load_yaml(input)
    # assert
    assert actual == expected
