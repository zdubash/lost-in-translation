"""
The test library of Lost in Translation, a translation evaluation engine and
Olin College Software Design final project.

See README for required dependencies.

Authors: Zarius Dubash, Annie Sheil

Note: we admit that these tests are non-exhaustive. That said, this project was
actually inspired by the unit-testing flow of testing that reversing a function
would be equivalent to its original input.

We consider the entire program a unit test, and as a result these tests simply
check for errors in accessing translations. We hope you understand.
"""

import pytest
import helpers

fr_test_phrases = {
    "This is a test": "C'est un test",
    "I really like baguettes": "J’aime vraiment baguettes",
    "Can you understand me?": "Pouvez-vous me comprendre?",
    "I can speak two languages": "Je peux parler deux langues",
    "Context is important": "Contexte est important",
    "This is a short sentence": "Il s’agit d’une courte phrase",
}

lang_codes = ["ar", "fr", "th", "de", "ja", "ru", "nl", "fi", "da", "sv"]


def test_mm_translator_usage():
    """
    Test to ensure MyMemory translator is providing actual translations, not an
    "out of translations" warning.
    """
    for key in fr_test_phrases:
        assert helpers.mm_translator(key, "en", "fr")[:16] != "MYMEMORY \
            WARNING"


def test_get_translation():
    """
    Test to ensure no exceptions are occuring when attempting to fetch
    translations from all three sources (if an error occurred, get_translation
    would crash and not return a list)
    """

    for lang in lang_codes:
        assert type(helpers.get_translation("Hello world", "en", lang)) == list
