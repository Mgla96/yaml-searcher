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


def test_dict_search_success_get_val_from_arr_index():
    # arrange
    key = "hello[0]"
    expected = "hi"
    d = {"hello": [expected, "world"]}

    # act
    actual = dict_search(d, key)

    # assert
    assert actual == expected


def test_dict_search_success_get_val_from_arr_index_2():
    # arrange
    key = "hello[0].hi[-1]"
    d = {"hello": [{"hi": ["alpha", "beta", "gamma"]}, "world"]}
    expected = "gamma"

    # act
    actual = dict_search(d, key)

    # assert
    assert actual == expected


def test_dict_search_failure_get_val_from_nonexistent_arr_index():
    # arrange
    key = "hello[0]"
    expected = None
    d = {"hello": "world"}

    # act
    actual = dict_search(d, key)

    # assert
    assert actual == expected
