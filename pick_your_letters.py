"""
Made by Ze Sheng
"""

import random
import string


def read_from_file(file_name):
    """
    Reads all words from file
    Parameter file_name is the name of the file
    This function returns a list containing all the words
    """
    f = open(file_name, "r")
    all_words = f.read().splitlines()
    f.close()
    return all_words


def ask_for_length():
    """
    In the beginning of a game, the player should input the length of the word.
    All valid inputs should be an integer from 3 to 10, inclusive.
    This function does not accept any invalid input until a valid one is input.
    """
    # TODO: define the length of the word
    while True:
        input_hint = "Enter a number between 3 - 10 to be length of the word you are going to guess:"
        length = input(input_hint + '\n').strip()
        if length.isnumeric():
            l = int(length)
            if 3 <= l <= 10:
                print("The length of the word is", length + '\n')
                return l
            else:
                print('Please input integer between 3 - 10. \n')
        else:
                print('Invalid Input! Please make sure that your input is an integer between 3 - 10. \n')



def filter_word_list(all_words, length):
    """
    Filter the words having a specific length.
    """
    # TODO use a list to store all the valid words for a game

    print("Initializing words pool......")
    valid_words = []
    for word in all_words:
        if len(word) == length:
            valid_words.append(word)
    print('Game Start')
    print('---------------------------------------------------------------------')
    return valid_words


def set_up(length):
    """
    Creates a main pile of 26 * length cards, represented as a list of lowercase
    letters, with length of each letter
    """
    # TODO create a main pile using 26 * length cards and create a discard pile using an empty list
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
    main_pile = letters * length
    discard_pile = []
    return main_pile, discard_pile


def shuffle_cards(pile):
    """
    This function shuffles the given pile and doesn’t return anything
    """
    # TODO use random.shuffle() to shuffle the pile
    random.shuffle(pile)


def move_to_discard_pile(discard_pile, card):
    """
    Move the given card to the top of the discard pile
    Parameter discard_pile is the discard pile
    Parameter card is the given letter to be discarded
    This function doesn’t return anything
    """
    # TODO use .insert() method to insert the card
    discard_pile.insert(0, card)


def deal_initial_cards(main_pile, discard_pile, length):
    """
    The computer is always the first person that gets dealt to and always plays first.
    Deal one card to the computer, one to the user, one to the computer, one to
    the user, and so on.
    Remove the card on top of the main pile and put it on the discard pile
    This function returns a tuple containing two lists, the first one representing
    the human’s hand and the second one representing the computer’s hand
    """
    # TODO create hand cards for human and computer by using two lists and then deal cards
    computer_hand_cards = []
    human_hand_cards = []
    deal_times = 0
    while deal_times < length:
        # deal one card to the computer:
        computer_hand_cards.append(main_pile.pop(0))
        # deal one to the user:
        human_hand_cards.append(main_pile.pop(0))
        # move to the next turn
        deal_times += 1

    # Remove the card on top of the main pile and put it on the discard pile
    discard_pile.append(main_pile.pop(0))
    return human_hand_cards, computer_hand_cards


def get_first_from_pile_and_remove(pile):
    """
    Return and remove the first item of the given list
    Parameter pile is the list from which to remove the first element
    """
    # TODO use .pop() method to remove the first letter
    return pile.pop(0)


def check_bricks(main_pile, discard_pile):
    """
    Check whether the main_pile is empty.
    If so, shuffles the discard_pile and moves all the cards to the main_pile. Then
    turn over the top card of the main_pile to be the start of the new discard_pile.
    Otherwise, do nothing.
    """
    # TODO check if the main pile is empty, if so, refill it
    if not main_pile:
        for card in discard_pile:
            main_pile.append(card)
        discard_pile.clear()
        shuffle_cards(main_pile)
        discard_pile.append(main_pile.pop(0))


def get_similarity(w1, w2):
    """
    Compute the similarity of str1 and str2
    """
    w1 = list(w1)
    w2 = list(w2)
    same_number = 0
    for i in range(0, len(w1)):
        if w1[i] == w2[i]:
            same_number += 1
    return same_number / len(w1)


def find_target(computer_hand_cards, computer_target_list, similarity, idx, old_target):
    """
    Input is current hand of computer, find the nearest target word as its target word.
    """
    current_word = ''.join(computer_hand_cards)
    current_max_similarity = similarity
    word_max_similarity_index = idx
    target = old_target
    i = 0
    target = old_target
    while i < len(computer_target_list):
        new_similarity = get_similarity(current_word, computer_target_list[i])
        if current_max_similarity < new_similarity:
            target = computer_target_list[i]
            current_max_similarity = new_similarity
            word_max_similarity_index = i
        i += 1

    return target, current_max_similarity


def computer_play(computer_hand_cards, computer_target_list, main_pile, discard_pile):
    """
    Computer's turn. Try to make it clever.
    Here I use a function to calculate the similarity between two words
    It return a number from 0 (no letter is same) to 1 (all letters are same)
    Computer's strategy:
    1. find a current target
    2. check any bad letters: v, x, q, z
    3. looking at incoming letters from DISCARD to change bad letters
        3.1: the incoming one is also bad -> check the top letter from MAIN PILE
    4. if there is no bad letter, find a new target using the current incoming letter from DISCARD PILE
    5. if there is no good target, try to check the top one from MAIN PILE
    6  if this card could lead to a better result, take it!
    7. if no, remain the same hands
    """
    # TODO
    print('Computers\' turn\n')
    print('Computer\'s current hand is: \n')
    print(computer_hand_cards)
    current_word = ''.join(computer_hand_cards)
    current_max_similarity = 0
    word_max_similarity_index = 0

    i = 0
    while i < len(computer_target_list):
        new_similarity = get_similarity(current_word, computer_target_list[i])
        # case 1: found an exactly same word:
        if new_similarity == 1:
            print('Computer does not took any letter from DISCARD PILE\n')
            print('Computer does not took any letter from MAIN PILE\n')
            return computer_hand_cards
        # case 2: no exactly same word, find a word having the largest similarity
        elif current_max_similarity < new_similarity:
            current_max_similarity = new_similarity
            word_max_similarity_index = i
        i += 1

    has_bad_letter = False
    bad_letters = ['x', 'v', 'z', 'k', 'w', 'q', 'j']
    bad_end_letters = ['c', 'i', 'l', 'j']
    bad_second_letters = ['b', 'f', 'g', 'h', 'j', 'y']
    bad_letters2 = ['x', 'v', 'j', 'v', 'z', 'q', 'y']
    bad_letters_idx = 0
    if len(computer_hand_cards) > 4:
        for l in computer_hand_cards:
            # check the end first
            if computer_hand_cards[len(computer_hand_cards) - 1] in bad_end_letters or computer_hand_cards[1] in bad_second_letters:
                has_bad_letter = True
                if computer_hand_cards[len(computer_hand_cards) - 1] in bad_end_letters:
                    bad_letters_idx = len(computer_hand_cards) - 1
                else:
                    bad_letters_idx = 1
                break
            if l in bad_letters:
                has_bad_letter = True
                bad_letters_idx = computer_hand_cards.index(l)

    elif len(computer_hand_cards) == 4:
        for l in computer_hand_cards:
            # check the end first
            if computer_hand_cards[len(computer_hand_cards) - 1] in bad_end_letters or computer_hand_cards[1] in bad_second_letters:
                has_bad_letter = True
                if computer_hand_cards[len(computer_hand_cards) - 1] in bad_end_letters:
                    bad_letters_idx = len(computer_hand_cards) - 1
                else:
                    bad_letters_idx = 1
                break
            if l in bad_letters2:
                has_bad_letter = True
                bad_letters_idx = computer_hand_cards.index(l)


    # Set a target word to computer:
    target_word = computer_target_list[word_max_similarity_index]
    #print(target_word)
    # Then look at the incoming letter from DISCARD PILE and find a position to insert:
    incoming_letter = discard_pile[0]
    incoming_letter2 = main_pile[0]
    #print('Incoming is a', incoming_letter, 'from DISCARD PILE')
    similarity = current_max_similarity
    insert_idx = 0
    take_the_discard_letter = False
    new_target_word = target_word
    target_list = []
    similarity_list = []
    incoming_letter_from_main = main_pile[0]

    # Highest priority : check if the game is over:
    for i in range(0, len(computer_hand_cards)):
        tmp = computer_hand_cards[i]
        discard_letter = computer_hand_cards[i]
        computer_hand_cards[i] = incoming_letter
        current_word = ''.join(computer_hand_cards)
        for j in range(0, len(computer_target_list)):
            similarity = get_similarity(current_word, computer_target_list[j])
            if similarity == 1:
                new_letter = discard_pile.pop(0)
                print('Computer took', new_letter, 'from DISCARD PILE')
                computer_hand_cards[i] = new_letter
                print('Computer put', discard_letter, 'into DISCARD PILE')
                discard_pile.insert(0, discard_letter)
                print('Computer\'s current hand is:')
                print(computer_hand_cards)
                print('---------------------------------------------------------------------')
                return computer_hand_cards
        computer_hand_cards[i] = tmp

    for i in range(0, len(computer_hand_cards)):
        tmp = computer_hand_cards[i]
        discard_letter = computer_hand_cards[i]
        computer_hand_cards[i] = incoming_letter2
        current_word = ''.join(computer_hand_cards)
        for j in range(0, len(computer_target_list)):
            similarity = get_similarity(current_word, computer_target_list[j])
            if similarity == 1:
                print('Computer did not take any letter from DISCARD PILE')
                new_letter = main_pile.pop(0)
                print('Computer took', new_letter, 'from MAIN PILE')
                computer_hand_cards[i] = new_letter
                print('Computer put', discard_letter, 'into DISCARD PILE')
                discard_pile.insert(0, discard_letter)
                print('Computer\'s current hand is:')
                print(computer_hand_cards)
                print('---------------------------------------------------------------------')
                return computer_hand_cards
        computer_hand_cards[i] = tmp

    # Second-highest Priority - check bad letters
    if has_bad_letter and incoming_letter not in bad_letters:
        if (bad_letters_idx == len(computer_hand_cards) - 1 and incoming_letter not in bad_end_letters) or (bad_letters_idx == 1 and incoming_letter not in bad_second_letters):
            new_letter = discard_pile.pop(0)
            print('Computer took', new_letter, 'from DISCARD PILE')
            discard_letter = computer_hand_cards[bad_letters_idx]
            computer_hand_cards[bad_letters_idx] = new_letter
            print('Computer put', discard_letter, 'into DISCARD PILE')
            discard_pile.insert(0, discard_letter)
            print('Computer\'s current hand is:')
            print(computer_hand_cards)
            print('---------------------------------------------------------------------')
            return computer_hand_cards
        elif (bad_letters_idx == len(computer_hand_cards) - 1 and incoming_letter_from_main not in bad_letters and incoming_letter_from_main not in bad_end_letters) or (bad_letters_idx == 1 and incoming_letter_from_main not in bad_letters and incoming_letter_from_main not in bad_second_letters):
            print('Computer did not take any letter from DISCARD PILE')
            new_letter = main_pile.pop(0)
            print('Computer took', new_letter, 'from MAIN PILE')
            discard_letter = computer_hand_cards[bad_letters_idx]
            computer_hand_cards[bad_letters_idx] = new_letter
            print('Computer put', discard_letter, 'into DISCARD PILE')
            discard_pile.insert(0, discard_letter)
            print('Computer\'s current hand is:')
            print(computer_hand_cards)
            print('---------------------------------------------------------------------')
            return computer_hand_cards
        new_letter = discard_pile.pop(0)
        print('Computer took', new_letter, 'from DISCARD PILE')
        discard_letter = computer_hand_cards[bad_letters_idx]
        computer_hand_cards[bad_letters_idx] = new_letter
        print('Computer put', discard_letter, 'into DISCARD PILE')
        discard_pile.insert(0, discard_letter)
        print('Computer\'s current hand is:')
        print(computer_hand_cards)
        print('---------------------------------------------------------------------')
        return computer_hand_cards
    elif has_bad_letter and incoming_letter_from_main not in bad_letters:
        print('Computer did not take any letter from DISCARD PILE')
        new_letter = main_pile.pop(0)
        print('Computer took', new_letter, 'from MAIN PILE')
        discard_letter = computer_hand_cards[bad_letters_idx]
        computer_hand_cards[bad_letters_idx] = new_letter
        print('Computer put', discard_letter, 'into DISCARD PILE')
        discard_pile.insert(0, discard_letter)
        print('Computer\'s current hand is:')
        print(computer_hand_cards)
        print('---------------------------------------------------------------------')
        return computer_hand_cards

    # update new target
    for i in range(0, len(computer_hand_cards)):
        tmp = computer_hand_cards[i]
        discard_letter = computer_hand_cards[i]
        computer_hand_cards[i] = incoming_letter
        new_target_word, similarity = find_target(computer_hand_cards, computer_target_list,
                                                  current_max_similarity, word_max_similarity_index, target_word)
        similarity_list.append(similarity)
        # print(similarity_list)
        if similarity_list[i] > current_max_similarity:
            #print(new_target_word, target_word)
            take_the_discard_letter = True
            insert_idx = i
            break
        computer_hand_cards[i] = tmp
    # Take the top letter from DISCARD PILE, computer MUST insert this letter
    if take_the_discard_letter:
        new_letter = discard_pile.pop(0)
        print('Computer took', new_letter, 'from DISCARD PILE')
        computer_hand_cards[insert_idx] = new_letter
        print('Computer put', discard_letter, 'into DISCARD PILE')
        discard_pile.insert(0, discard_letter)

    # Computer does not take the letter from DISCARD PILE -> Reveal a letter from MAIN PILE:
    else:
        # Take a look at the letter from MAIN PILE:
        print('Computer did not take any letter from DISCARD PILE')
        incoming_letter = main_pile[0]
        similarity = current_max_similarity
        insert_idx = 0
        take_the_main_letter = False
        similarity_list = []
        discard_letter = computer_hand_cards[insert_idx]
        #print('Incoming is a', incoming_letter, 'from MAIN PILE')

        for i in range(0, len(computer_hand_cards)):
            tmp = computer_hand_cards[i]
            discard_letter = computer_hand_cards[i]
            computer_hand_cards[i] = incoming_letter
            new_target_word, similarity = find_target(computer_hand_cards, computer_target_list,
                                                      similarity, word_max_similarity_index, target_word)
            similarity_list.append(similarity)
            # print(similarity_list)
            if similarity_list[i] > current_max_similarity:
                print(new_target_word, target_word)
                take_the_main_letter = True
                insert_idx = i
                break
            computer_hand_cards[i] = tmp
        # case 1: pick the letter from MAIN PILE:
        if take_the_main_letter:
            new_letter = main_pile.pop(0)
            print('Computer took', new_letter, 'from MAIN PILE')
            computer_hand_cards[insert_idx] = new_letter
            print('Computer put', discard_letter, 'into DISCARD PILE')
            discard_pile.insert(0, discard_letter)

        # case 2: does not pick the letter from MAIN PILE:
        else:
            discard_pile.insert(0, main_pile.pop(0))
            print('Computer did not take any letter from MAIN PILE')
    print('Computer\'s current hand is:')
    print(computer_hand_cards)
    print('---------------------------------------------------------------------')
    return computer_hand_cards


def human_play(human_hand_cards, human_target_list, main_pile, discard_pile, length):
    """
    Human's turn
    """
    # TODO
    check_bricks(main_pile, discard_pile)
    print('Your turn\n')
    print('Your word list is:')
    print( human_hand_cards)
    print('Pick \'' + str(discard_pile[0]) + '\' from DISCARD PILE or reveal another letter from MAIN PILE')
    # print(discard_pile, '\n')
    human_response = ask_d_or_m('Input \'D/d\' to pick it from DISCARD PILE. '
                                'Input \'M/m\' to pick another letter from MAIN PILE: \n')
    # test:
    #human_response = False
    # get a card from discard pile or main pile
    if human_response: # discard pile
        new_card = discard_pile.pop(0)
        print('You get a letter', new_card, 'from DISCARD PILE')
        # replace this card to a card having a specific index
        replaced_card_idx = ask_for_the_letter_to_be_replaced(length)
        move_to_discard_pile(discard_pile, human_hand_cards[replaced_card_idx])
        #print(discard_pile)
        human_hand_cards[replaced_card_idx] = new_card
    else: # main pile
        new_card = main_pile.pop(0)
        print('You get a letter \'' + str(new_card) + '\' from MAIN PILE')
        replace_or_not = ask_yes_or_no('Do you want to accept this letter? '
                                       'Type \'y/yes\' to accept, \'n/no\' to discard.\n')
        #replace_or_not = False
        if replace_or_not:
            idx = ask_for_the_letter_to_be_replaced(length)
            move_to_discard_pile(discard_pile, human_hand_cards[idx])
            human_hand_cards[idx] = new_card
        else: # discard this letter:
            move_to_discard_pile(discard_pile, new_card)
    print('Your word list is: \n', human_hand_cards)
    print('----------------------------------------------------------------')
    #print(discard_pile)
    return human_hand_cards


def ask_for_the_letter_to_be_replaced(length):
    """
    Ask for the index of the letter that the user wants to replace
    Prompt again if the input index is out of range or invalid
    Parameter length is the number of cards in the human’s hand
    This function returns the index of the letter to be replaced
    """
    # TODO use a while loop to get the index of the card that will be replaced

    while True:
        input_hint = "Input the index of the letter to be replaced, from 0 - {}".format(length - 1)
        idx = input(input_hint + '\n').strip()
        if idx.isnumeric():
            idx = int(idx)
            if 0 <= idx < length:
                return idx
            else:
                print('Please input integer between 0 - ', length - 1, '!:\n')
        else:
            print('Invalid Input! Please make sure that your input is an integer between 0 -', length - 1, '! \n')


def ask_d_or_m(msg):
    """
    Displays msg and get user's response
    Prompt again if the input is invalid
    Parameter msg is the message to display
    """
    # TODO get human's input, if it is valid, then return. Otherwise it will wait until a valid input.
    while True:
        human_input = input(msg).strip()
        # corner case:
        if len(human_input) == 0:
            print('Invalid input! Type \'D/d\' or \'M/m\' \n')
        elif human_input[0] == 'm' or human_input[0] == 'M':
            return False
        elif human_input[0] == 'd' or human_input[0] == 'D':
            return True
        else:
            print('Invalid input! Type \'D/d\' or \'M/m\' \n')


def ask_yes_or_no(msg):
    """
    Displays msg and get user's response
    Prompt again if the input is invalid
    Parameter msg is the message to display
    This function returns True if the user answers ‘y’ or ‘yes’, and returns False if
    the user answers ‘n’ or ‘no’
    """
    # TODO get human's input, if it is valid, then return. Otherwise it will wait until a valid input.
    while True:
        human_input = input(msg).strip()
        if len(human_input) == 0:
            print('Invalid input! Type \'y/yes\' to accept, \'n/no\' to discard.\n')
        elif human_input[0] == 'n' or human_input[0] == 'N':
            return False
        elif human_input[0] == 'y' or human_input[0] == 'Y':
            return True
        else:
            print('Invalid input! Type \'y/yes\' to accept, \'n/no\' to discard.\n')


def check_game_over(human_hand_cards, computer_hand_cards, words_with_specific_length):
    """
    Check if the game is end:
    Case 1 (Human wins): If human_hand_cards is a word in the words pool but computer_hand_cards is not.
    Case 2 (Computer wins): If computer_hand_cards is a word in the words pool but human_hand_cards is not.
    Case 3 (Tie): Both two set of cards are in the words pool.
    """
    # TODO use two boolean flags to determine whether the game ends
    human_flag = False
    computer_flag = False

    human_word = ''.join(human_hand_cards)
    computer_word = ''.join(computer_hand_cards)

    # Determine whether words are in the pool
    if human_word in words_with_specific_length:
        human_flag = True
    if computer_word in words_with_specific_length:
        computer_flag = True

    # case 1: tie
    if human_flag and computer_flag:
        print('Game End! There is a tie.')
        return True

    # case 2: Human wins
    if not computer_flag and human_flag:
        print('Game End! You win!! Your word is,', human_word, 'Congratulations!')
        return True

    # case 3: computer wins
    if not human_flag and computer_flag:
        print('Game End! Computer Wins!! Its word is', computer_word, '.')
        return True


def main():
    # reads all words from file
    all_words = read_from_file("words.txt")

    print("Welcome to the game!")

    # ask for a number as the length of the word
    # TODO: call ask_for_length() to check the length of word and print the length.
    word_length = ask_for_length()
    print("Try to get the words with {} letters".format(word_length))

    # filter all_words with a length equal to the given length
    # TODO call filter_word_list() to filter all valid words
    all_valid_words = filter_word_list(all_words, word_length)

    # set up main_pile and discard_pile
    # TODO a tuple is used to store two piles. Call set_up to build two piles
    (main_pile, discard_pile) = set_up(word_length)

    # shuffle main pile
    # TODO call shuffle_cards() to shuffle the main pile
    shuffle_cards(main_pile)

    # deal cards to players, creating human_hand_cards and computer_hand_cards
    # and initialize discard pile
    # TODO call deal_initial_cards() to deal cards
    (human_hand_cards, computer_hand_cards) = deal_initial_cards(main_pile, discard_pile, word_length)
    #return 0
    # start the game
    while True:
        # check if main_pile is empty by calling check_bricks(main_pile, discard_pile)
        check_bricks(main_pile, discard_pile)

        # computer play goes here
        # TODO let computer play first by calling call computer_play()
        computer_hand_cards = computer_play(computer_hand_cards, all_valid_words, main_pile, discard_pile)

        # human play goes here
        # TODO use a helper function like computer_play() to simulate the player
        human_hand_cards = human_play(human_hand_cards, all_valid_words, main_pile, discard_pile, word_length)

        # check if game is over and print out results
        # TODO call check_game_over to check whether game is over:
        isOver = check_game_over(human_hand_cards, computer_hand_cards, all_valid_words)

        if isOver:
            break

if __name__ == "__main__":
    main()
