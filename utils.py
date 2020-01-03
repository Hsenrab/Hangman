import random

import words


def pick_word():
    chosen_word = random.choice(words.word_options)
    return chosen_word


def is_input_single_letter(input_letter):
    input_as_list = list(input_letter)
    num_letters = len(input_as_list)

    if num_letters != 1 or not input_as_list[0].isalpha():
        return False
    else:
        return True


class HangmanWord:
    def __init__(self, word):
        self.hidden_word = list(word)
        self.player_word = ["_" for char in self.hidden_word]
        self.letters_tried = []

    def create_printable_hidden_word(self):
        print_string = ""
        for char in self.hidden_word:
            print_string = print_string + char + " "

        return print_string

    def create_printable_player_word(self):
        print_string = ""
        for char in self.player_word:
            print_string = print_string + char + " "

        return print_string

    def is_letter_correct(self, letter):
        self.letters_tried.append(letter)
        letter_found = False

        for index, char in enumerate(self.hidden_word):
            if char == letter:
                letter_found = True
                self.player_word[index] = letter

        return letter_found

    def has_letter_been_tried(self, letter):
        return letter in self.letters_tried

    def is_word_complete(self):
        return self.hidden_word == self.player_word


