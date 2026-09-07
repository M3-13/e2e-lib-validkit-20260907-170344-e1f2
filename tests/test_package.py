"""Verify the package skeleton: imports, exports and function signatures."""

import inspect

import validkit

EXPECTED = {
    "is_valid_email": (["text"], bool),
    "luhn_check": (["digits"], bool),
    "is_valid_iban": (["text"], bool),
    "is_valid_isbn13": (["text"], bool),
    "normalize_phone": (["text", "country_code"], str),
    "strip_accents": (["text"], str),
    "mask_secret": (["text", "keep"], str),
    "slugify": (["text"], str),
    "clamp": (["value", "low", "high"], float),
}


def test_public_import_statement_works():
    from validkit import (
        clamp,
        is_valid_email,
        is_valid_iban,
        is_valid_isbn13,
        luhn_check,
        mask_secret,
        normalize_phone,
        slugify,
        strip_accents,
    )

    funcs = (
        is_valid_email,
        luhn_check,
        is_valid_iban,
        is_valid_isbn13,
        normalize_phone,
        strip_accents,
        mask_secret,
        slugify,
        clamp,
    )
    assert all(callable(f) for f in funcs)
    assert {f.__name__ for f in funcs} == set(EXPECTED)


def test_each_function_has_contract_signature():
    for name, (params, returns) in EXPECTED.items():
        func = getattr(validkit, name)
        sig = inspect.signature(func)
        assert list(sig.parameters) == params
        assert sig.return_annotation is returns


def test_mask_secret_default_keep_is_four():
    sig = inspect.signature(validkit.mask_secret)
    assert sig.parameters["keep"].default == 4
