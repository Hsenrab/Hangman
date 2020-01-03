

def welcome():
    print("Welcome to Hangman")
    print("What is your name?")
    name = input()
    print("Hello", name)
    print("Let's begin:")


def display_length(hangman_word):
    print("The word I am thinking of has", len(hangman_word.hidden_word), "letters.")


def display_player_word(hangman_word):
    print("Current state: ", hangman_word.create_printable_player_word())


def ask_player_for_letter(hangman_word):

    valid_letter_given = False
    while not valid_letter_given:
        print("Please choose a letter")
        letter = input()

        if not hangman_word.has_letter_been_tried(letter):
            valid_letter_given = True
        else:
            print("You have already tried that letter")

    return letter


def letter_correct(letter):
    print("Yes!", letter, "is in my word")


def letter_incorrect(letter):
    print("Sorry", letter, "is not in my word")


def display_number_of_lives(num_lives):
    print("You have", num_lives, "lives remaining")


def game_won(hangman_word):
    print("You Win!, you guessed the word", hangman_word.create_printable_player_word(), "in time!")


