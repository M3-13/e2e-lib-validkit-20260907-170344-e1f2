"""E-mail address validation."""

import re

from validkit._validation import _reject_overlong

_EMAIL_RE = re.compile(r"^(?!.*\.\.)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def is_valid_email(text: str) -> bool:
    """Return ``True`` if *text* is a formally valid e-mail address.

    The check is purely syntactic: exactly one ``@``, a non-empty local part, and
    a domain containing at least one dot with valid characters on either side.
    No network or DNS access is performed.
    """
    _reject_overlong(text)
    return _EMAIL_RE.fullmatch(text) is not None
