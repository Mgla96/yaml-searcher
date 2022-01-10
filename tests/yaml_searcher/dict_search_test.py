from yamlsearcher.yaml_searcher import dict_search


def test_dict_search_success_none():
    # arrange
    expected = None
    # act
    actual = dict_search({}, "hi")
    # assert
    assert actual == expected


def test_dict_search_success_key():
    # arrange
    key = "hello"
    expected = "world"
    d = {key: expected}

    # act
    actual = dict_search(d, "hello")

    # assert
    assert actual == expected


def test_dict_search_failure_no_key():
    # arrange
    key = "hello"
    expected = None
    d = {key: "world"}

    # act
    actual = dict_search(d, "other")

    # assert
    assert actual == expected
