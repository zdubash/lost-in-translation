"""
A library of helper functions for a translation project.

Authors: Zarius Dubash, Annie Sheil
"""

import translators as ts

from translate import Translator


def new_translator(phrase, src, dest):
    # uses microsoft for when MyMemory limit has been reached
    # translator = Translator(provider='microsoft', secret_access_key="bfbfd764b8bd4be9b6b2dd60c369c491", from_lang=src, to_lang=dest)

    translator = Translator(from_lang=src, to_lang=dest)
    return translator.translate(phrase)


baiducodes = {"fr": "fra", "ar": "ara", "en": "en", "th": "th", "de": "de", "ja": "jp", "ru": "ru", "nl": "nl", "fi": "fin", "da": "dan", "sv": "swe"}


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
        new_translator(phrase, src, dest), 
        ts.baidu(phrase, baiducodes[src], baiducodes[dest], sleep_seconds=0.1),
    ]


def reverse_translation(phraseList, src):
    """
    Translate a list of strings back into English using the same translation engine.

    Args:
        phraseList: a List of Strings, the phrases to translate
        src: the language code of the current language of the phrases

    Returns: a List of Strings, the phrases after translation back into English.
    """

    translations = []
    i = 0
    for phrase in phraseList:
        translations.append(get_translation(phrase, "en", src)[i])
        i += 1
    return translations


# bing: 'en': ['af', 'ar', 'as', 'bn', 'bs', 'bg', 'yue', 'ca', 'zh-Hans', 'zh-Hant', 'hr', 'cs', 'da', 'prs', 'nl', 'en', 'et', 'fj', 'fil', 'fi', 'fr', 'fr-ca', 'de', 'el', 'gu', 'ht', 'he', 'hi', 'mww', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'kn', 'kk', 'tlh-Latn', 'tlh-Piqd', 'ko', 'ku', 'kmr', 'lv', 'lt', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'nb', 'or', 'ps', 'fa', 'pl', 'pt', 'pt-pt', 'pa', 'otq', 'ro', 'ru', 'sm', 'sr-Cyrl', 'sr-Latn', 'sk', 'sl', 'es', 'sw', 'sv', 'ty', 'ta', 'te', 'th', 'to', 'tr', 'uk', 'ur', 'vi', 'cy', 'yua'],
# alibaba: 'en': ['zh', 'ru', 'es', 'fr', 'ar', 'tr', 'pt', 'th', 'id', 'vi']
# baidu: 'en': ['zh', 'ara', 'est', 'bul', 'pl', 'dan', 'de', 'ru', 'fra', 'fin', 'kor', 'nl', 'cs', 'rom', 'pt', 'jp', 'swe', 'slo', 'th', 'wyw', 'spa', 'el', 'hu', 'it', 'yue', 'cht', 'vie'],
