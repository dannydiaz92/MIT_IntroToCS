# 6.00 Problem Set 3A
#
# The 6.00 Word Game


import random
import string
import sys

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7  #number of letters dealt

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

#Converting words into dictionary representation
#Takes string -> dictionary
# Given
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list "hello"
    return: dictionary {'h':1, 'e':1, 'l':2, 'o':1}
    """
    # freq: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1  # if the key (char) is not present, return 0 for value
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    n: integer (HAND_SIZE , hand size required for additional points)
    returns: int >= 0.
    """
    # TO DO...

    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    if len(word) == n:
        score = score * len(word) + 50
    else:
        score *= len(word)
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line


#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...

    # Only difference with solution is line:
    # new_hand = hand.copy()

    for i in word:
        hand[i] -= 1

    return hand

    #return new_hand

    new_hand = hand.copy()
    for letter in word:
        new_hand[letter] -= 1
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings (list of valid words from words.txt)
    """
    # TO DO...

    #assume all letters in hand
    #corrected version

    #word_dict: dictionary representation of the user's word

    if word not in word_list:
        return False

    word_as_dict = get_frequency_dict(word)

    #print "the word is : ", word
    #print "word_dict: ", word_as_dict
    #print "hand: ", hand

    for letter in word_as_dict.keys():
        print "letter: ", letter
        if hand.get(letter, 0) < word_as_dict[letter]:
            return False

    return True


def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    # TO DO ...

    # Rewriting

    starting_handlen = calculate_handlen(hand)
    t_score = 0

    while calculate_handlen(hand) > 0:
        print 'Current hand: \n', display_hand(hand)
        word = raw_input('Enter a word from letters above or enter a "." if finished: ')
        if word == '.':
            print 'Total score: %d points' % t_score
            return
        else:
            valid_word = is_valid_word(word, hand, word_list)
            if not valid_word:
                print 'The word entered is not a valid word\n'
                print 'Please enter a word composed of only letters in hand \n'
            else: # if valid
                word_score = get_word_score(word, starting_handlen)
                t_score += word_score
                print '"%s" earned %d points. Total: %d points' % (word, word_score, t_score)
                hand = update_hand(hand, word)

    print 'No letters left. Total score: %d points.' % total

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO...


    #initialize hand for choice == r

    hand = deal_hand(HAND_SIZE)

    while True:

        choice = raw_input('''Hello choose from the following options: \n
                       \'n\': Play new hand\n
                        \'r\': Play last hand\n
                        \'e\': Exit game\n
                      ''')

        if choice == 'n':
            hand = deal_hand(HAND_SIZE)
            print 'inside play_hand'
            print 'the hand chosen is: %s' % hand
            print 'playing the hand: play_hand() '
            play_hand(hand.copy(), word_list)
            print
        elif choice == 'r':
            play_hand(hand.copy(), word_list)
        elif choice == 'e':
            'Exiting the game'
            break
        else:
            print 'Invalid choice'




#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
