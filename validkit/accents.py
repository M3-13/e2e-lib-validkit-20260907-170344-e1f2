"""Diacritic removal."""

import unicodedata

from validkit._validation import _reject_overlong

_SHARP_S = {
    "ß": "ss",
    "ẞ": "SS",
}


def strip_accents(text: str) -> str:
    """Return ``text`` with diacritical marks removed.

    The input is normalized to NFD, which splits accented characters into a base
    letter and one or more combining marks; every combining mark of Unicode
    category ``Mn`` is then dropped. German sharp s (``ß``/``ẞ``) does not
    decompose, so it is expanded to ``ss``/``SS`` explicitly. Any other
    character (punctuation, hyphens, whitespace) is left untouched.
    """
    _reject_overlong(text)

    expanded = "".join(_SHARP_S.get(ch, ch) for ch in text)
    decomposed = unicodedata.normalize("NFD", expanded)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
