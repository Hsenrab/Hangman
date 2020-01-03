import random

import words


def pick_word():
    chosen_word = random.choice(words.word_options)
    return chosen_word
