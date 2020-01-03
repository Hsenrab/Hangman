import utils
import interaction
import store

num_lives = len(store.ascii_man)

interaction.welcome()
play_again=True

while play_again:
    # Pick hidden word and initialise
    hangman_word = utils.HangmanWord(utils.pick_word())

    # Tell player word length
    interaction.display_length(hangman_word)
    interaction.display_number_of_lives(num_lives)
    interaction.display_player_word(hangman_word)


    while num_lives > 0:
        # Ask player for a letter
        letter = interaction.ask_player_for_letter(hangman_word)

        # Determine if letter is correct
        is_correct = hangman_word.is_letter_correct(letter)

        if is_correct:
            interaction.letter_correct(letter)

            if hangman_word.is_word_complete():
                break
        else:
            num_lives = num_lives - 1
            interaction.letter_incorrect(letter)

        interaction.display_number_of_lives(num_lives)
        interaction.display_player_word(hangman_word)

    if hangman_word.is_word_complete():
        interaction.game_won(hangman_word)
    else:
        interaction.game_lost(hangman_word)

    play_again = interaction.ask_if_play_again()


interaction.goodbye()
