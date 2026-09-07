"""Luhn checksum validation."""

from validkit._validation import _reject_overlong


def luhn_check(digits: str | int) -> bool:
    """Return whether ``digits`` passes the Luhn checksum.

    Accepts a string or an integer. For string input the overlong guard runs
    first; spaces and hyphens are then stripped and the remaining characters
    must all be digits. Empty or non-digit input yields ``False``. A value of
    any other type raises ``TypeError`` with a message that never includes the
    supplied value.
    """
    if isinstance(digits, str):
        _reject_overlong(digits)
        cleaned = digits.replace(" ", "").replace("-", "")
    elif isinstance(digits, bool):
        raise TypeError("expected a string or integer input")
    elif isinstance(digits, int):
        cleaned = str(digits)
    else:
        raise TypeError("expected a string or integer input")

    if not cleaned:
        return False
    if not cleaned.isdigit():
        return False

    total = 0
    for idx, ch in enumerate(reversed(cleaned)):
        digit = int(ch)
        if idx % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0
