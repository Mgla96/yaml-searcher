from yamlsearcher.yaml_searcher import dictionary_search


def test_dictionary_search_success_none():
    # arrange
    expected = None
    # act
    actual = dictionary_search({}, "hi")
    # assert
    assert actual == expected


def test_dictionary_search_success_val():
    # arrange
    key = "hello"
    expected = "world"
    d = {key: expected}

    # act
    actual = dictionary_search(d, "hello")

    # assert
    assert actual == expected
