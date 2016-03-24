from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

    #Redoing

    WordPermutations = []

    for length in range(1, HAND_SIZE + 1):
       # Get the permutations of this length
        perms = get_perms(hand, length)

        # Store the permutations in the list we initialized earlier

        WordPermutations.extend(perms)

        maxScore = 0
        maxWord = None

        for word in WordPermutations:
            if word in word_list:
                p_score = get_word_score(word, HAND_SIZE)

                if p_score > maxScore:
                    maxScore = p_score
                    maxWord = word

        return maxWord


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...

    #redoing

    original_handlen = calculate_handlen(hand)
    total = 0
    while calculate_handlen(hand) > 0:
        print 'Current Hand: ',
        display_hand(hand)
        computerWord = comp_choose_word(hand, word_list)
        if computerWord == None:
            break
    else:
        point = get_word_score(computerWord, original_handlen)
        total += point
        print '"%s" earned %d points. Total: %d points' % (computerWord, point, total)

        hand = update_hand(hand, computerWord)
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...

    hand = deal_hand(HAND_SIZE)
    while True:

        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        while cmd != 'n' and cmd != 'r' and cmd != 'e':
            print "Invalid command."
            cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        if cmd == 'e':
            break

        player = raw_input('Enter u to have yourself play, c to have the computer play: ')
        while player != 'u' and player != 'c':
            print "Invalid command."
            player = raw_input('Enter u to have yourself play, c to have the computer play: ')

        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)

        if player == 'u':
            play_hand(hand.copy(), word_list)
        else:
            comp_play_hand(hand.copy(), word_list)
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
