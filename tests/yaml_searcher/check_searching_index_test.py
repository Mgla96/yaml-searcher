from yamlsearcher.yaml_searcher import check_search_index


def test_check_search_index_success():
    # arrange
    expected = ("a", 0)
    search = "a[0]"

    # act
    actual = check_search_index(search)

    # assert
    assert actual == expected
    assert len(actual) == 2


def test_check_search_index_no_index_success():
    # arrange
    expected = ("a", None)
    search = "a"

    # act
    actual = check_search_index(search)

    # assert
    assert actual == expected
    assert len(actual) == 2
