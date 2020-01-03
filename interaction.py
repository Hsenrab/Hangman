

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


def ask_player_for_letter():
    print("Please choose a letter")
    letter = input()
    return letter


def letter_correct(letter):
    print("Yes!,", letter, "is in my word")


def letter_incorrect(letter):
    print("Sorry", letter, "is not in my word")


def display_number_of_lives(num_lives):
    print("You have", num_lives, "lives remaining")
