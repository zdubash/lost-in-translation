"""
A library of helper functions for Lost in Translation, a translation evaluation
engine and Olin College Software Design final project.

See README for required dependencies.

Authors: Zarius Dubash, Annie Sheil
"""

import translators as ts  # pip install translators
from translate import Translator  # pip install translate

# Insert your email address here:
user_email = "YOUR_EMAIL_HERE@email.com"


def mm_translator(phrase, src, dest):
    """
    Get translation from MyMemory translation engine.

    Args:
        phrase: a String, the phrase to be translated
        src: the language code of the current language of the phrase
        dest: the language code of the destination language

    Returns:
        a String, the translation of the given phrase
    """
    translator = Translator(from_lang=src, to_lang=dest, email=user_email)
    return translator.translate(phrase)


baiducodes = {
    "fr": "fra",
    "ar": "ara",
    "en": "en",
    "th": "th",
    "de": "de",
    "ja": "jp",
    "ru": "ru",
    "nl": "nl",
    "fi": "fin",
    "da": "dan",
    "sv": "swe",
}


def get_translation(phrase, dest, src):
    """
    Get translations of a phrase from three translation engines.

    Args:
        phrase: a String, the phrase to be translated
        dest: the language code of the destination language
        src: the language code of the current language of the phrase

    Returns:
        a List of three Strings, different translations of the given phrase.
    """

    return [
        ts.bing(phrase, src, dest, if_use_cn_host=False),
        mm_translator(phrase, src, dest),
        ts.baidu(phrase, baiducodes[src], baiducodes[dest], sleep_seconds=0.1),
    ]


def reverse_translation(phraseList, src):
    """
    Translate a list of strings back into English using the same translation
    engine.

    Args:
        phraseList: a List of Strings, the phrases to translate
        src: the language code of the current language of the phrases

    Returns:
        a List of Strings, the phrases after translation back into English.
    """

    translations = []
    i = 0
    for phrase in phraseList:
        translations.append(get_translation(phrase, "en", src)[i])
        i += 1
    return translations
