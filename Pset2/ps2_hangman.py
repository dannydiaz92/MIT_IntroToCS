# 6.00 Problem Set 3
# 
# Hangman
#

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file

    #Python 2 format
    #inFile = open(WORDLIST_FILENAME, 'r', 0)

    #Python 3
    inFile = open(WORDLIST_FILENAME, 'r')

    # line: string
    line = inFile.readline()
    
    # wordlist: list of strings
    ## wordlist = string.split(line)  #(python 2 format)

    #Python 3
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

#Computer selects random word
word = choose_word(wordlist)

print("the secret word is: ", word)

#Initalize the number of guesses (tries)
guesses = 8

#List of available letters
avail_letters = list(string.ascii_lowercase)

#Pattern '_ _ _ _'
pattern = '_ '*len(word)

#Set of letters in word
word_letters = set(word)

print("Welcome to the game of Hangman!")
print("I am thinking of a word that is : ", len(word), " letters long")
print("--------------------")



# While have not
# 1) exhausted guesses and
# 2) Have not completed word
while (guesses > 0) and (len(word_letters) != 0):
    print("You have ", guesses, " guesses left.")
    print("Available letters: ", ''.join(avail_letters))

    user_input = input("Please guess a letter: ").lower()


    if (user_input in word) and (user_input in avail_letters):

        del avail_letters[avail_letters.index(user_input)]
        word_letters.remove(user_input)

        char_index = [index for index, char in enumerate(word) if char == user_input]

        print('index in word where letter is found: ', char_index)

        #Trying doing this with a list comprehension
        for letter_index in char_index:
            pattern = pattern[:letter_index*2] + user_input + pattern[letter_index*2 + 1:]

        print("Good guess: ", pattern)

        print('-----------')

    elif user_input not in avail_letters:
        print("Already used that word. Please choose a word in available letters.")

    else:
        print("Oops! That letter is not in my word: ", pattern)

        del avail_letters[avail_letters.index(user_input)]

        print('-----------')

    guesses -= 1

if len(word_letters) == 0:
    print("Congrats, you won!")




