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
    expected = "hello: world\n"
    # act
    actual = format_output(input)
    # assert
    assert actual == expected


def test_format_output_arr_success():
    # arrange
    input = ["hello", "world"]
    expected = "- hello\n- world\n"
    # act
    actual = format_output(input)
    # assert
    assert actual == expected
