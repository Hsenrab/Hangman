import random

import words


def pick_word():
    chosen_word = random.choice(words.word_options)
    return chosen_word


class HangmanWord:
    def __init__(self, word):
        self.hidden_word = list(word)
        self.player_word = ["_" for char in self.hidden_word]

    def create_printable_player_word(self):
        print_string = ""
        for char in self.player_word:
            print_string = print_string + char + " "

        return print_string
