"""Tests for validkit.accents.strip_accents."""

import pytest

from validkit.accents import strip_accents


def test_removes_umlauts_and_expands_sharp_s():
    result = strip_accents("Grüße aus Zürich \u2013 Straße")
    assert "ü" not in result
    assert "ä" not in result
    assert "ö" not in result
    assert "ß" not in result
    assert result == "Grusse aus Zurich \u2013 Strasse"


def test_removes_common_accents():
    assert strip_accents("café naïve résumé") == "cafe naive resume"


def test_leaves_punctuation_and_hyphens_unchanged():
    assert strip_accents("a-b \u2013 c, d; e: f! g? h.") == "a-b \u2013 c, d; e: f! g? h."


def test_leaves_plain_ascii_unchanged():
    assert strip_accents("hello world 123") == "hello world 123"


def test_empty_string_returns_empty_string():
    assert strip_accents("") == ""


def test_uppercase_sharp_s_expands_to_ss():
    assert strip_accents("STRASSE ẞ") == "STRASSE SS"


def test_non_string_input_raises_type_error_without_value():
    for value in (123, None, 3.14, ["Grüße"], {"text": "x"}):
        with pytest.raises(TypeError) as exc:
            strip_accents(value)
        assert "123" not in str(exc.value)
        assert str(value) not in str(exc.value)


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError):
        strip_accents("a" * 5000)


def test_4096_characters_is_accepted():
    text = "a" * 4096
    assert strip_accents(text) == text


def test_error_messages_do_not_contain_input_value():
    with pytest.raises(ValueError) as exc:
        strip_accents("á" * 5000)
    assert "á" not in str(exc.value)
