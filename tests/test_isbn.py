"""Tests for validkit.isbn.is_valid_isbn13."""

import pytest

from validkit.isbn import is_valid_isbn13


def test_valid_isbn13_with_hyphens():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_plain_digits():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_wrong_check_digit_is_false():
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_too_few_digits_is_false():
    assert is_valid_isbn13("978-3-16-148410") is False


def test_too_many_digits_is_false():
    assert is_valid_isbn13("978-3-16-148410-00") is False


def test_empty_string_is_false():
    assert is_valid_isbn13("") is False


def test_non_digit_characters_is_false():
    assert is_valid_isbn13("978-3-16-14841X-0") is False


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(9783161484100)  # type: ignore[arg-type]


def test_type_error_message_omits_input_value():
    with pytest.raises(TypeError) as excinfo:
        is_valid_isbn13(123)  # type: ignore[arg-type]
    assert "123" not in str(excinfo.value)


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_isbn13("1" * 5000)
