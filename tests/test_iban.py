"""Tests for IBAN validation."""

import pytest

from validkit.iban import is_valid_iban


def test_valid_german_iban():
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_iban_with_spaces():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_other_countries():
    assert is_valid_iban("GB82WEST12345698765432") is True
    assert is_valid_iban("FR1420041010050500013M02606") is True


def test_invalid_check_digit():
    assert is_valid_iban("DE89370400440532013001") is False


def test_invalid_length():
    assert is_valid_iban("DE8937040044053201300") is False
    assert is_valid_iban("DE893704004405320130000") is False


def test_empty_string():
    assert is_valid_iban("") is False


def test_invalid_country_code():
    assert is_valid_iban("XX89370400440532013000") is False


def test_invalid_character_set():
    assert is_valid_iban("DE8937040044053201300!") is False
    assert is_valid_iban("DE89370400440532-13000") is False


def test_lowercase_is_invalid():
    assert is_valid_iban("de89370400440532013000") is False


def test_wrong_type_raises_typeerror():
    with pytest.raises(TypeError):
        is_valid_iban(123)  # type: ignore[arg-type]


def test_wrong_type_message_does_not_leak_value():
    with pytest.raises(TypeError) as exc:
        is_valid_iban(123)  # type: ignore[arg-type]
    assert "123" not in str(exc.value)


def test_overlong_input_raises_valueerror():
    with pytest.raises(ValueError):
        is_valid_iban("A" * 5000)
