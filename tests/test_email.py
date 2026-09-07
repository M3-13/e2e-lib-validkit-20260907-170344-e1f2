"""Tests for validkit.email.is_valid_email."""

import pytest

from validkit.email import is_valid_email


@pytest.mark.parametrize(
    "email",
    [
        "a@b.co",
        "john.doe@example.com",
        "first.last+tag@sub.domain.org",
        "user_name@example.co",
        "a@b.cd",
    ],
)
def test_valid_emails_return_true(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "",
        "a@b",
        "plainaddress",
        "@missinglocal.co",
        "missingatsign.co",
        "a@b.co@extra",
        "a b@c.com",
        "a@.co",
        "a@b.",
        "a@b..co",
        "a@@b.co",
        "a@b.co ",
        "a@b.co\n",
    ],
)
def test_invalid_emails_return_false(email):
    assert is_valid_email(email) is False


def test_special_characters_rejected():
    assert is_valid_email("a@b.co!") is False
    assert is_valid_email("!a@b.co") is False
    assert is_valid_email("a@b c.co") is False


def test_exactly_one_at_sign():
    assert is_valid_email("a@b@c.co") is False


def test_wrong_type_raises_type_error_without_value():
    for bad in (123, None, 4.5, ["a@b.co"], b"a@b.co"):
        with pytest.raises(TypeError) as exc:
            is_valid_email(bad)
        message = str(exc.value)
        assert "123" not in message
        assert "a@b.co" not in message


def test_overlong_input_raises_value_error():
    with pytest.raises(ValueError) as exc:
        is_valid_email("a" * 5000)
    assert "a" * 5000 not in str(exc.value)


def test_boundary_4096_chars_does_not_raise():
    local = "a" * 4090
    assert is_valid_email(local + "@b.co") is True


def test_just_over_4096_raises_value_error():
    with pytest.raises(ValueError):
        is_valid_email("a" * 4097)
