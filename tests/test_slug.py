"""Tests for validkit.slug.slugify."""

import pytest

from validkit.slug import slugify


def test_slugify_basic_umlauts():
    assert slugify("Grüße aus Zürich!") == "gruesse-aus-zuerich"


def test_slugify_lowercases_and_hyphenates_spaces():
    assert slugify("Hello World") == "hello-world"


def test_slugify_dangerous_path_loses_slashes_and_dots():
    result = slugify("../etc/passwd")
    assert "/" not in result
    assert "." not in result


def test_slugify_strips_leading_trailing_hyphens():
    assert slugify("  --hello--  ") == "hello"


def test_slugify_collapses_duplicate_hyphens():
    assert slugify("a---b---c") == "a-b-c"


def test_slugify_allows_digits():
    assert slugify("Version 2.0 release") == "version-2-0-release"


def test_slugify_result_restricted_to_allowed_charset():
    result = slugify("ÄäÖöÜüß !@#$%^&*()")
    assert all(c in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in result)


def test_slugify_empty_string():
    assert slugify("") == ""


def test_slugify_only_special_characters():
    assert slugify("!!!") == ""


def test_slugify_strips_accents_generally():
    assert slugify("Café") == "cafe"


def test_slugify_rejects_wrong_type():
    with pytest.raises(TypeError):
        slugify(123)


def test_slugify_wrong_type_message_omits_value():
    with pytest.raises(TypeError) as exc_info:
        slugify(123)
    assert "123" not in str(exc_info.value)


def test_slugify_rejects_overlong_input():
    with pytest.raises(ValueError):
        slugify("a" * 5000)
