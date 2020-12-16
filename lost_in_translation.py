"""
The main library of Lost in Translation, a translation evaluation engine and
Olin College Software Design final project.

See README for required dependencies.

Authors: Zarius Dubash, Annie Sheil
"""

import helpers


class LostInTranslation:
    """
    Representation of a translation evaluation engine.
    """

    def __init__(self):
        """
        Create a new LostInTranslation instance.
        """
        self._complete = False

    def set_complete(self, state):
        """
        Set variable complete to either true or false (default false).

        Args:
            state: a Boolean value to set complete variable to
        """
        self._complete = state

    def process_text(self, phrase, dest, src):
        """
        Process given text and translate as necessary.

        Args:
            phrase: a String to translate
            dest: a String, the language code to translate to
            src: a String, the language code to translate from
        """
        print(f"Translating from {src} to {dest}.\n")
        translations = helpers.get_translation(phrase, dest, src)
        print(
            f"Bing: {translations[0]}\nMyMemory: {translations[1]}\nBaidu: \
{translations[2]}\n"
        )
        return translations

    def process_reverse(self, phrases, src):
        """
        Process given text and translate back to English.

        Args:
            phrases: a List of Strings to translate
            src: a String, the language code to translate from
        """
        print("Translating back to English...\n")
        reverse_translations = helpers.reverse_translation(phrases, src)
        print(
            f"Bing: {reverse_translations[0]}\nMyMemory: \
{reverse_translations[1]}\nBaidu: {reverse_translations[2]}\n"
        )
        return reverse_translations

    def process_translations(self, phrases, dest, src):
        """
        Process given text and translate as necessary.

        Args:
            phrases: a List of Strings to translate
            dest: a String, the language code to translate to
            src: a String, the language code to translate from
        """
        print(f"Translating from {src} to {dest}.\n")
        translations = []
        i = 0
        for phrase in phrases:
            translations.append(helpers.get_translation(phrase, dest, src)[i])
            i += 1
        print(
            f"Bing: {translations[0]}\nMyMemory: {translations[1]}\nBaidu: \
{translations[2]}\n"
        )
        return translations


class Controller:
    """
    Generic controller for Lost in Translation.
    """

    def get_input(self):
        """
        Generic input function
        """
        pass


class TextController(Controller):
    """
    Text-based controller for Lost in Translation.
    """

    def get_input(
        self,
        message="To translate again, enter another language code, otherwise \
press Enter to translate back to English.\n"):
        """
        Process input given a message to provide to user.

        Args:
            message: a String, presented to the user when taking input

        Returns: stripped user input, in String format
        """
        user_input = input(message)
        stripped_user_input = user_input.strip()
        return stripped_user_input


def main():
    """
    Run the Lost in Translation userflow.
    """
    translate = LostInTranslation()
    controller = TextController()

    while not translate._complete:
        processed_response = controller.get_input(
            "\nEnter a phrase in English here: ")

        if processed_response is not None:
            processed_lang = controller.get_input(
                "\nEnter the language code to translate into: \
                    \n[ar, fr, th, de, ja, ru, nl, fi, da, sv]\n"
            )
            translation = translate.process_text(
                processed_response, processed_lang, "en"
            )
            processed_next_lang = controller.get_input()
            while processed_next_lang not in ["", "en"]:
                translation = translate.process_translations(
                    translation, processed_next_lang, processed_lang
                )
                processed_lang = processed_next_lang
                processed_next_lang = controller.get_input()

            translate.process_reverse(translation, processed_lang)
            translate.set_complete(True)

    print("Thank you for using LostInTranslation!")


if __name__ == "__main__":
    main()
