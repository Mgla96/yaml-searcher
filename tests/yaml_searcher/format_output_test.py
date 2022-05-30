from yamlsearcher.yaml_searcher import format_output


def test_format_output_str_success():
    # arrange
    input = expected = "value"

    # act
    actual = format_output(input)

    # assert
    assert actual == expected


def test_format_output_dict_success():
    # arrange
    input = {"hello": "world"}
    expected = "hello: world"

    # act
    actual = format_output(input)

    # assert
    assert actual == expected


def test_format_output_arr_success():
    # arrange
    input = ["hello", "world"]
    expected = "- hello\n- world"

    # act
    actual = format_output(input)

    # assert
    assert actual == expected


def test_format_output_int_success():
    # arrange
    input = 5
    expected = 5

    # act
    actual = format_output(input)

    # assert
    assert actual == expected


def test_format_output_float_success():
    # arrange
    input = 5.55
    expected = 5.55

    # act
    actual = format_output(input)

    # assert
    assert actual == expected
