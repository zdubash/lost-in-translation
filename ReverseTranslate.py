import helpers, time

class ReverseTranslate:
    """
    Representation of a translation evaluation engine.
    """

    def __init__(self):
        """
        Create a new ReverseTranslate instance.
        """
        pass

    def complete(self):
        """
        Check whether the translation is finished.

        Returns:
            True if the translation is complete and False otherwise.
        """

        return False

    def process_text(self, phrase, dest, src):
        """
        Process given text and translate as necessary.
        """

        translations = helpers.get_translation(phrase, dest, src)
        print("Bing: " + translations[0] + "\nAlibaba: " + translations[1] + "\nBaidu: " + translations[2])
        return translations

    def process_reverse(self, phrases, src):
        """
        Process given text and translate as necessary.
        """

        reverse_translations = helpers.reverse_translation(phrases, src)
        print("\nBing: " + reverse_translations[0] + "\nAlibaba: " + reverse_translations[1] + "\nBaidu: " + reverse_translations[2])
        return reverse_translations

    def process_translation(self, phrases, dest, src):
        """
        Process given text and translate as necessary.
        """
        pass
        translations = helpers.get_translation(phrase, dest, src)
        print("Bing: " + translations[0] + "\nAlibaba: " + translations[1] + "\nBaidu: " + translations[2])
        return translations


class View:
    """
    Generic view for Translator.

    Attributes:
        _translate: a ReverseTranslator instance.
    """

    def __init__(self, translate):
        """
        Create an instance of a View for a translation.

        Args:
            translate: a ReverseTranslator instance.
        """
        self._translate = translate

    def draw(self):
        """
        Display the translation to the user.
        """
        pass

class TextView(View):
    """
    Text-based view for a Reverse Translation.
    """

    def draw(self):
        """
        Print the representation of the game to standard output.
        """
        pass


class Controller:
    """
    Generic controller for translation.
    """

    def get_input(self):
        """
        Translate (ha) input from the user into usable data.

        (either a String to translate, or a char for most useful translation/whether to repeat)
        """
        pass

class TextController(Controller):
    """
    Text-based controller for a Reverse Translation.
    """
    # Add static methods here for different print functions.

    def get_input(self):
        """
        Process input (blah blah)
        """
        user_input = input()
        stripped_user_input = user_input.strip()
        # lang_input = input("Which language code would you like to translate to? ")
        # stripped_lang_input = lang_input.strip()
        
        # return [stripped_user_input, stripped_lang_input]
        return stripped_user_input


def main():
    """
    Run the main game.

    Play a one-player game of Set. In each step of the game, print out the
    current board and get the player's input. Check this input, and if the
    player guesses a possible set, check the cards to confirm that this is the
    case. If the cards form a set, remove them from the board and draw new
    cards from the deck.
    """
    translate = ReverseTranslate()
    view = TextView(translate)
    controller = TextController()

    while not translate.complete():

        # Show the current state of the translation and get the user's inout.
        view.draw()
        print("Enter a phrase in English here: ")
        processed_response = controller.get_input()

        # If the player made a guess, check if the selected cards are a set and
        # remove them from the board if they are.
        if processed_response is not None:
            print("Enter the language code to translate into: ")
            processed_lang = controller.get_input()
            translation = translate.process_text(processed_response, processed_lang, "en")
            print("To translate again, enter another language code, otherwise press Enter. ")
            processed_second_lang = controller.get_input()
            if processed_second_lang != "":
                translate.process_text(translation, processed_second_lang, processed_lang)
            else:
                translate.process_reverse(translation, processed_lang)
                break

    print("Thank you for using ReverseTranslate!")


if __name__ == "__main__":
    main()