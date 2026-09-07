"""Tests for validkit.luhn.luhn_check."""

import pytest

from validkit.luhn import luhn_check


def test_valid_luhn_number_returns_true():
    assert luhn_check("79927398713") is True


def test_invalid_luhn_number_returns_false():
    assert luhn_check("79927398710") is False


def test_integer_input():
    assert luhn_check(79927398713) is True
    assert luhn_check(79927398710) is False


def test_spaces_and_hyphens_are_ignored():
    assert luhn_check("7992 7398 713") is True
    assert luhn_check("7992-7398-713") is True
    assert luhn_check(" 79927398713 ") is True


def test_empty_input_returns_false():
    assert luhn_check("") is False


def test_whitespace_only_returns_false():
    assert luhn_check("   ") is False


def test_non_digit_input_returns_false():
    assert luhn_check("7992739871A") is False
    assert luhn_check("abc") is False


def test_single_zero_returns_true():
    assert luhn_check("0") is True


def test_wrong_type_raises_typeerror():
    with pytest.raises(TypeError):
        luhn_check(3.14)  # type: ignore[arg-type]


def test_wrong_type_message_excludes_input_value():
    with pytest.raises(TypeError) as exc_info:
        luhn_check(None)  # type: ignore[arg-type]
    assert "None" not in str(exc_info.value)


def test_overlong_string_raises_valueerror():
    with pytest.raises(ValueError):
        luhn_check("7" * 5000)
