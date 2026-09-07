"""URL slug generation."""

import re
import unicodedata

from validkit._validation import _reject_overlong

# German umlauts and sharp-s that expand to two characters, so they must be
# transliterated before general accent stripping.
_GERMAN_MAP = {
    "ä": "ae",
    "ö": "oe",
    "ü": "ue",
    "ß": "ss",
}

# Single character class with no nested quantifiers: no backtracking risk.
_NON_WORD_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Return a URL-safe slug for *text*.

    Lowercases the input, transliterates umlauts, strips remaining accents,
    replaces every run of non-``[a-z0-9]`` characters with a single hyphen and
    drops leading, trailing and duplicate hyphens. The result contains only
    characters from ``[a-z0-9-]``.
    """
    _reject_overlong(text)

    text = text.lower()
    for accent, replacement in _GERMAN_MAP.items():
        text = text.replace(accent, replacement)

    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))

    text = _NON_WORD_RE.sub("-", text)
    return text.strip("-")
