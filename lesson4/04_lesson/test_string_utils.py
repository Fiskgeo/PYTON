import pytest
from string_utils import StringUtils
string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Skypro", "Skypro"),
    ("    Hello world", "Hello world"),
    (" Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   +", "+"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Skypro", "S", True),
    ("Hello world", "w", True),
    ("123abc", "2", True),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("123abc", "Q", False),
    ("", "1", False),
    ("+++", "*", False),
])
def test_contains_negative(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Skypro", "S", "kypro"),
    ("Hello world", "w", "Hello orld"),
    ("123abc", "2", "13abc"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("123abc", "Q", "123abc"),
    ("", "1", ""),
    ("+++", "*", "+++"),
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected