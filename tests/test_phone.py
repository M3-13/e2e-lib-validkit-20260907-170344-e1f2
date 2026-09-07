"""Tests for ``validkit.phone.normalize_phone``."""

import pytest

from validkit.phone import normalize_phone


def test_german_number_with_formatting():
    assert normalize_phone("030 1234567", "DE") == "+49301234567"


def test_german_number_with_punctuation():
    assert normalize_phone("030-123-4567", "DE") == "+49301234567"


def test_number_without_leading_zero():
    assert normalize_phone("301234567", "DE") == "+49301234567"


def test_country_code_is_case_insensitive():
    assert normalize_phone("030 1234567", "de") == "+49301234567"


def test_country_code_with_surrounding_whitespace():
    assert normalize_phone("030 1234567", "  DE ") == "+49301234567"


def test_other_country_code():
    assert normalize_phone("01 2345678", "AT") == "+4312345678"


def test_multiple_leading_zeros_only_one_stripped():
    assert normalize_phone("001234", "DE") == "+4901234"


def test_non_digit_characters_removed():
    assert normalize_phone("(0)30-123 4567 ext. 89", "DE") == "+4930123456789"


def test_boundary_exactly_4096_chars():
    assert normalize_phone("9" * 4096, "DE") == "+49" + "9" * 4096


def test_boundary_over_4096_chars_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("9" * 4097, "DE")


def test_empty_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("", "DE")


def test_whitespace_only_text_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("   ", "DE")


def test_text_without_digits_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("abc", "DE")


def test_lone_zero_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0", "DE")


def test_unknown_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("030 1234567", "ZZ")


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(1234567, "DE")


def test_non_string_country_code_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone("030 1234567", 49)


def test_error_message_never_contains_input_value():
    secret = "030 1234567"
    with pytest.raises(ValueError) as exc_info:
        normalize_phone(secret, "ZZ")
    assert secret not in str(exc_info.value)
    assert "ZZ" not in str(exc_info.value)


def test_error_message_never_contains_phone_digits():
    with pytest.raises(ValueError) as exc_info:
        normalize_phone("0", "DE")
    assert "0" not in str(exc_info.value)
