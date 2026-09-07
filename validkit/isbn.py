"""ISBN-13 validation."""

from validkit._validation import _reject_overlong


def is_valid_isbn13(text: str) -> bool:
    """Return ``True`` if ``text`` is a valid ISBN-13, otherwise ``False``.

    Hyphens and spaces are ignored. A valid ISBN-13 has exactly 13 digits whose
    weighted modulo-10 check digit matches the last digit.
    """
    _reject_overlong(text)

    cleaned = text.replace("-", "").replace(" ", "")
    if len(cleaned) != 13 or not cleaned.isdigit():
        return False

    weighted_sum = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(cleaned))
    return weighted_sum % 10 == 0
