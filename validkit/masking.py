"""Secret masking."""

from validkit._validation import _reject_overlong


def mask_secret(text: str, keep: int = 4) -> str:
    """Mask all but the last ``keep`` characters of ``text`` with ``*``.

    The final ``keep`` characters stay visible; everything before them is
    replaced by asterisks. ``keep=0`` masks the whole string, and a ``keep``
    greater than or equal to the string length also masks it completely, so
    the full plaintext is never returned.
    """
    _reject_overlong(text)

    if isinstance(keep, bool) or not isinstance(keep, int):
        raise TypeError("keep must be an integer")
    if keep < 0:
        raise ValueError("keep must be a non-negative integer")

    if keep == 0 or keep >= len(text):
        return "*" * len(text)

    return "*" * (len(text) - keep) + text[-keep:]
