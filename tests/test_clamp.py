"""Tests for validkit.clamp."""

import pytest

from validkit import clamp


def test_value_within_bounds_is_returned():
    assert clamp(5, 1, 10) == 5


def test_value_below_low_returns_low():
    assert clamp(-3, 1, 10) == 1


def test_value_above_high_returns_high():
    assert clamp(99, 1, 10) == 10


def test_value_equal_to_low_returns_low():
    assert clamp(1, 1, 10) == 1


def test_value_equal_to_high_returns_high():
    assert clamp(10, 1, 10) == 10


def test_float_inputs():
    assert clamp(2.5, 1.0, 10.0) == 2.5
    assert clamp(0.5, 1.0, 10.0) == 1.0
    assert clamp(20.0, 1.0, 10.0) == 10.0


def test_int_inputs_preserve_int_type():
    result = clamp(5, 1, 10)
    assert isinstance(result, int)
    assert result == 5

    result = clamp(-3, 1, 10)
    assert isinstance(result, int)
    assert result == 1

    result = clamp(99, 1, 10)
    assert isinstance(result, int)
    assert result == 10


def test_negative_bounds():
    assert clamp(-5, -10, -1) == -5
    assert clamp(-20, -10, -1) == -10
    assert clamp(0, -10, -1) == -1


def test_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(5, 10, 1)


def test_value_error_message_hides_numbers():
    with pytest.raises(ValueError) as exc_info:
        clamp(5, 10, 1)
    message = str(exc_info.value)
    assert "5" not in message
    assert "10" not in message
    assert "1" not in message


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        clamp("5", 1, 10)
    with pytest.raises(TypeError):
        clamp(5, "1", 10)
    with pytest.raises(TypeError):
        clamp(5, 1, "10")
