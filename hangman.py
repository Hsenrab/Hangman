import utils
import interaction

num_lives = 10

interaction.welcome()

# Pick hidden word and initialise
hangman_word = utils.HangmanWord(utils.pick_word())

# Tell player word length
interaction.display_length(hangman_word)
interaction.display_player_word(hangman_word)
interaction.display_number_of_lives(num_lives)


while num_lives > 0:
    # Ask player for a letter
    letter = interaction.ask_player_for_letter()

    # Determine if letter is correct
    is_correct = hangman_word.is_letter_correct(letter)

    if is_correct:
        interaction.letter_correct(letter)
    else:
        num_lives = num_lives - 1
        interaction.letter_incorrect(letter)

    interaction.display_player_word(hangman_word)
    interaction.display_number_of_lives(num_lives)

