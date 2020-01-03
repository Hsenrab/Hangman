import utils

hangman = utils.HangmanWord("frog")
print(hangman.create_printable_player_word())

hangman.player_word[2] = "o"
print(hangman.create_printable_player_word())

hangman.player_word[0] = "o"
print(hangman.create_printable_player_word())

hangman.player_word[3] = "o"
print(hangman.create_printable_player_word())


hangman = utils.HangmanWord("froggy")
print(hangman.create_printable_player_word())

hangman.player_word[2] = "o"
print(hangman.create_printable_player_word())

hangman.player_word[5] = "o"
print(hangman.create_printable_player_word())

hangman.player_word[4] = "o"
print(hangman.create_printable_player_word())