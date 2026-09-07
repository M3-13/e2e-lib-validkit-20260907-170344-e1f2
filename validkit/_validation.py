"""Shared validation helpers for the validkit package."""


def _reject_overlong(text: str) -> None:
    """Reject string inputs longer than 4096 characters before any processing.

    Raises a ``ValueError`` whose message never includes the supplied value, or a
    ``TypeError`` for non-string input.
    """
    if not isinstance(text, str):
        raise TypeError("expected a string input")
    if len(text) > 4096:
        raise ValueError("input exceeds the maximum allowed length of 4096 characters")
