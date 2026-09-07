"""Phone number normalization to E.164 format."""

import re

from validkit._validation import _reject_overlong

# ISO 3166-1 alpha-2 country code -> E.164 country calling code.
_COUNTRY_CODES = {
    "DE": "49",
    "AT": "43",
    "CH": "41",
    "FR": "33",
    "IT": "39",
    "ES": "34",
    "PT": "351",
    "NL": "31",
    "BE": "32",
    "LU": "352",
    "GB": "44",
    "IE": "353",
    "DK": "45",
    "SE": "46",
    "NO": "47",
    "FI": "358",
    "PL": "48",
    "CZ": "420",
    "SK": "421",
    "HU": "36",
    "US": "1",
    "CA": "1",
    "MX": "52",
    "BR": "55",
    "AU": "61",
    "NZ": "64",
    "JP": "81",
    "CN": "86",
    "IN": "91",
    "RU": "7",
    "TR": "90",
    "ZA": "27",
}

# Matches a single non-digit character; no quantifiers, so no backtracking risk.
_NON_DIGITS = re.compile(r"\D")


def normalize_phone(text: str, country_code: str) -> str:
    """Normalize a phone number to E.164 format.

    ``text`` is expected in national format (optionally with a leading trunk
    prefix ``0``). All non-digit characters are removed, a single leading zero is
    stripped, and the result is prefixed with ``+`` and the country calling code
    for ``country_code`` (an ISO 3166-1 alpha-2 code, matched case-insensitively).
    """
    _reject_overlong(text)

    if not isinstance(country_code, str):
        raise TypeError("country_code must be a string")

    key = country_code.strip().upper()
    prefix = _COUNTRY_CODES.get(key)
    if prefix is None:
        raise ValueError("country_code must be a supported ISO 3166-1 alpha-2 code")

    digits = _NON_DIGITS.sub("", text)
    if not digits:
        raise ValueError("phone number must contain at least one digit")

    if digits[0] == "0":
        digits = digits[1:]

    if not digits:
        raise ValueError("phone number must contain digits after the trunk prefix")

    return "+" + prefix + digits
