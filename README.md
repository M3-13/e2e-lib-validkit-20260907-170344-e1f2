# validkit

Eine kleine, eigenständige Python-Bibliothek mit neun voneinander unabhängigen,
reinen Prüf- und Normalisierungsfunktionen. Sie nutzt ausschließlich die
Standardbibliothek, hat keine CLI, keine UI und keinen Netzwerkzugriff. Die
öffentliche API wird über `validkit/__init__.py` exportiert; jede Funktion ist
typannotiert, weist zu lange oder falsch typisierte Eingaben mit einem
aussagekräftigen Fehler ab und ist durch eigene pytest-Unit-Tests inklusive
Grenz- und Fehlerfällen abgedeckt.

## Tech-Stack

- **Sprache:** Python
- **Tests:** pytest
- **Laufzeit:** nur Standardbibliothek (keine externen Abhängigkeiten)

## Installation

Das Projekt benötigt keine externen Abhängigkeiten. Für die Ausführung der
Tests wird lediglich `pytest` benötigt:

```bash
pip install pytest
```

## Ausführung

Die Tests werden aus dem Repo-Wurzelverzeichnis gestartet:

```bash
pytest
```

## Verwendung

Alle Funktionen werden über das Paket importiert:

```python
from validkit import (
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
```

### Beispiele

| Funktion | Beispiel | Erwartete Ausgabe |
| --- | --- | --- |
| `is_valid_email` | `is_valid_email("a@b.co")` | `True` |
| `luhn_check` | `luhn_check("79927398713")` | `True` |
| `is_valid_iban` | `is_valid_iban("DE89370400440532013000")` | `True` |
| `is_valid_isbn13` | `is_valid_isbn13("978-3-16-148410-0")` | `True` |
| `normalize_phone` | `normalize_phone("030 1234567", "DE")` | `"+49301234567"` |
| `strip_accents` | `strip_accents("Grüße aus Zürich – Straße")` | `"Gruesse aus Zuerich – Strasse"` |
| `mask_secret` | `mask_secret("geheim123", keep=4)` | `"******123"` |
| `slugify` | `slugify("Grüße aus Zürich!")` | `"gruesse-aus-zuerich"` |
| `clamp` | `clamp(5, 1, 10)` | `5` |

### Verhaltensregeln

- Jede Funktion, die eine Zeichenkette entgegennimmt, weist Eingaben mit mehr
  als 4096 Zeichen vor der Verarbeitung mit einem `ValueError` ab.
- Fehlermeldungen nennen ausschließlich den Fehlertyp und die erwartete
  Eingabeform, niemals den übergebenen Wert.
- Ein falscher Eingabetyp führt zu einem `TypeError`.

## Features

- `is_valid_email` — Prüft eine E-Mail-Adresse.
- `luhn_check` — Prüft eine Ziffernfolge mit dem Luhn-Algorithmus.
- `is_valid_iban` — Prüft eine IBAN.
- `is_valid_isbn13` — Prüft eine ISBN-13.
- `normalize_phone` — Normalisiert eine Telefonnummer auf ein internationales Format.
- `strip_accents` — Entfernt Diakritika aus einem Text.
- `mask_secret` — Maskiert einen Geheimtext bis auf die letzten Zeichen.
- `slugify` — Erzeugt einen URL-Slug aus einem Text.
- `clamp` — Begrenzt einen Wert auf ein Intervall.
