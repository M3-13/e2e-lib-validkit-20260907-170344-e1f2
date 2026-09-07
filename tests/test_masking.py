"""Tests for validkit.masking.mask_secret."""

import pytest

from validkit.masking import mask_secret


def test_keeps_last_four_characters_by_default():
    assert mask_secret("geheim123") == "*****m123"


def test_keeps_last_keep_characters():
    assert mask_secret("geheim123", keep=4) == "*****m123"
    assert mask_secret("secret", keep=2) == "****et"
    assert mask_secret("abc", keep=1) == "**c"


def test_keep_zero_masks_everything():
    assert mask_secret("geheim123", keep=0) == "*********"


def test_keep_greater_than_length_masks_everything():
    assert mask_secret("abc", keep=5) == "***"


def test_keep_equal_to_length_masks_everything():
    assert mask_secret("abc", keep=3) == "***"


def test_empty_text_returns_empty_string():
    assert mask_secret("", keep=4) == ""


def test_negative_keep_raises_value_error_without_value():
    with pytest.raises(ValueError):
        mask_secret("geheim123", keep=-1)


def test_wrong_keep_type_raises_type_error():
    for bad in ("3", 4.0, None, [4]):
        with pytest.raises(TypeError):
            mask_secret("geheim123", keep=bad)


def test_bool_keep_is_rejected():
    with pytest.raises(TypeError):
        mask_secret("geheim123", keep=True)


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret(123)


def test_overlong_text_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("a" * 5000)


def test_error_messages_never_include_the_value():
    with pytest.raises(ValueError) as exc_info:
        mask_secret("geheim123", keep=-5)
    assert "geheim123" not in str(exc_info.value)
    assert "-5" not in str(exc_info.value)

    with pytest.raises(TypeError) as exc_info:
        mask_secret(123)
    assert "123" not in str(exc_info.value)
