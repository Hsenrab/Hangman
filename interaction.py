

def welcome():
    print("Welcome to Hangman")
    print("What is your name?")
    name = input()
    print("Hello", name)
    print("Let's begin:")


def display_length(word):
    print("The word I am thinking of has", len(word), "letters.")