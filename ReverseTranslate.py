def main():
    """
    Run the main game.

    Play a one-player game of Set. In each step of the game, print out the
    current board and get the player's input. Check this input, and if the
    player guesses a possible set, check the cards to confirm that this is the
    case. If the cards form a set, remove them from the board and draw new
    cards from the deck.
    """
    game = SetGame()
    view = TextView(game)
    controller = TextController()

    while not game.game_over():
        # Draw more cards if necessary.
        game.deal_cards()

        # Show the current state of the game and get the player's move.
        view.draw()
        processed_response = controller.get_input()

        # If the player made a guess, check if the selected cards are a set and
        # remove them from the board if they are.
        if processed_response is not None:
            game.process_guess(*processed_response)
    print("Deck is empty and no more sets can be found. Thanks for playing!")


if __name__ == "__main__":
    main()