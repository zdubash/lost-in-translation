"""
A library of helper functions for a translation project.

Authors: Zarius Dubash, Annie Sheil
"""

import translators as ts

baiducodes = {"fr": "fra", "ar": "ara", "en": "en", "th": "th"}


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
        ts.alibaba(phrase, src, dest), #supposed to be alibaba, change back
        ts.baidu(phrase, baiducodes[src], baiducodes[dest], sleep_seconds=0.1),
    ]

    # print(ts.bing(phrase, if_use_cn_host=False, from_language=src, to_language=dest)) # (working)
    # print(ts.alibaba(phrase, from_language=src, to_language=dest)) # (working)
    # print(ts.baidu(phrase, from_language=src, to_language=dest, sleep_seconds=0.1)) # (working but requires different codes)


def individual_translation(phrase, dest, src, engine):
    """
    Get a single phrase translation from the specified translation engine.

    Args:
        phrase: a String, the phrase to be translated
        dest: the language code of the destination language
        src: the language code of the current language of the phrase
        engine: the translation engine to use, either bing, alibaba, or baidu

    Returns:
        a String, the translation requested.
    """

    if engine == "bing":
        return ts.bing(phrase, src, dest, if_use_cn_host=False)
    if engine == "alibaba":
        return ts.alibaba(phrase, src, dest)
    if engine == "baidu":
        return ts.baidu(phrase, baiducodes[src], baiducodes[dest], sleep_seconds=0.1)


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


# bing: 'en': ['af', 'auto-detect', 'ar', 'auto-detect', 'as', 'auto-detect', 'bn', 'auto-detect', 'bs', 'auto-detect', 'bg', 'auto-detect', 'yue', 'auto-detect', 'ca', 'auto-detect', 'zh-Hans', 'auto-detect', 'zh-Hant', 'auto-detect', 'hr', 'auto-detect', 'cs', 'auto-detect', 'da', 'auto-detect', 'prs', 'auto-detect', 'nl', 'auto-detect', 'en', 'auto-detect', 'et', 'auto-detect', 'fj', 'auto-detect', 'fil', 'auto-detect', 'fi', 'auto-detect', 'fr', 'auto-detect', 'fr-ca', 'auto-detect', 'de', 'auto-detect', 'el', 'auto-detect', 'gu', 'auto-detect', 'ht', 'auto-detect', 'he', 'auto-detect', 'hi', 'auto-detect', 'mww', 'auto-detect', 'hu', 'auto-detect', 'is', 'auto-detect', 'id', 'auto-detect', 'ga', 'auto-detect', 'it', 'auto-detect', 'ja', 'auto-detect', 'kn', 'auto-detect', 'kk', 'auto-detect', 'tlh-Latn', 'auto-detect', 'tlh-Piqd', 'auto-detect', 'ko', 'auto-detect', 'ku', 'auto-detect', 'kmr', 'auto-detect', 'lv', 'auto-detect', 'lt', 'auto-detect', 'mg', 'auto-detect', 'ms', 'auto-detect', 'ml', 'auto-detect', 'mt', 'auto-detect', 'mi', 'auto-detect', 'mr', 'auto-detect', 'nb', 'auto-detect', 'or', 'auto-detect', 'ps', 'auto-detect', 'fa', 'auto-detect', 'pl', 'auto-detect', 'pt', 'auto-detect', 'pt-pt', 'auto-detect', 'pa', 'auto-detect', 'otq', 'auto-detect', 'ro', 'auto-detect', 'ru', 'auto-detect', 'sm', 'auto-detect', 'sr-Cyrl', 'auto-detect', 'sr-Latn', 'auto-detect', 'sk', 'auto-detect', 'sl', 'auto-detect', 'es', 'auto-detect', 'sw', 'auto-detect', 'sv', 'auto-detect', 'ty', 'auto-detect', 'ta', 'auto-detect', 'te', 'auto-detect', 'th', 'auto-detect', 'to', 'auto-detect', 'tr', 'auto-detect', 'uk', 'auto-detect', 'ur', 'auto-detect', 'vi', 'auto-detect', 'cy', 'auto-detect', 'yua'],
# alibaba: 'en': ['zh', 'ru', 'es', 'fr', 'ar', 'tr', 'pt', 'th', 'id', 'vi']
# baidu: 'en': ['zh', 'ara', 'est', 'bul', 'pl', 'dan', 'de', 'ru', 'fra', 'fin', 'kor', 'nl', 'cs', 'rom', 'pt', 'jp', 'swe', 'slo', 'th', 'wyw', 'spa', 'el', 'hu', 'it', 'yue', 'cht', 'vie'],
