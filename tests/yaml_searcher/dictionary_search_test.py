from yamlsearcher.yaml_searcher import dictionary_search


def test_dictionary_search_success_none():
    # arrange
    expected = None
    # act
    actual = dictionary_search({}, "hi")
    # assert
    assert actual == expected


def test_dictionary_search_success_key():
    # arrange
    key = "hello"
    expected = "world"
    d = {key: expected}

    # act
    actual = dictionary_search(d, "hello")

    # assert
    assert actual == expected


def test_dictionary_search_failure_no_key():
    # arrange
    key = "hello"
    expected = None
    d = {key: "world"}

    # act
    actual = dictionary_search(d, "other")

    # assert
    assert actual == expected
