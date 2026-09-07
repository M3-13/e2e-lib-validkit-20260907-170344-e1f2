"""Interval clamping."""

from numbers import Real


def clamp(value: float, low: float, high: float) -> float:
    if not isinstance(value, Real):
        raise TypeError("value must be a real number")
    if not isinstance(low, Real):
        raise TypeError("low must be a real number")
    if not isinstance(high, Real):
        raise TypeError("high must be a real number")
    if low > high:
        raise ValueError("low must be less than or equal to high")
    if value < low:
        return low
    if value > high:
        return high
    return value
