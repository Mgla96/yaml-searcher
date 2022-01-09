from yamlsearcher.yaml_searcher import check_search_val


def test_check_search_val_success():
    # arrange
    expected = "hello"
    # act
    actual = check_search_val(["python3", "hello"])
    # assert
    assert actual == expected


def test_check_search_val_arg_arr_greater_1_success():
    # arrange
    expected = "hello"
    # act
    actual = check_search_val(["python3", "hello", "world"])
    # assert
    assert actual == expected


def test_check_search_val_arg_arr_le_1_failure():
    # arrange
    expected = None
    # act
    actual = check_search_val(["python3"])
    # assert
    assert actual == expected
