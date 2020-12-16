# lost-in-translation

Welcome to Lost in Translation, a translation evaluation engine and Olin College Software Design final project by Zarius and Annie.

## Required dependencies:
* [translators](https://pypi.org/project/translators/): pip install translators
* [translate](https://pypi.org/project/translate/): pip install translate

## Usage:
* After installing dependencies, download both `lost-in-translation.py` and `helpers.py` from the GitHub Repo.
* Open `helpers.py` and input an email address under `user_email` in order to ensure that the MyMemory translation works properly.
* Then run the main file with `python lost-in-translation.py`.

Input any phrase, choose the various languages you’d like to use to translate it (one at a time), and watch how some of the words or the meaning may change as it reverts back to English at the end.

## Demo:
![Image](https://github.com/zdubash/lost-in-translation/raw/gh-pages/screen-recorder-tue-dec-15-2020-20-53-28.gif)

## Known Bugs:
* Some systems will struggle to display languages like Arabic, Japanese, and Thai, which don't use Roman script. However, lost-in-translation still works for these languages, just copy and paste the `[?]` symbols elsewhere on your system, like a word processor document, and they should render properly.
* Translations can take a while to load, as seen in the demo GIF above. Please be patient - we're fetching translations from the US (Bing), Italy (MyMemory), and China (Baidu)!

## Special Thanks:
We give thanks to Steve and the NINJA team for their help with this project as well as the entire course.
We also extend gratitude to the authors of [translators](https://pypi.org/project/translators/) and [translate](https://pypi.org/project/translate/), whose libraries are a key component of our project and were instrumental to our success.
