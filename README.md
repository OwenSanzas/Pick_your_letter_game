﻿# Pick_your_letter_game
 
## All Source Files:
### Controller File
* pick_your_letters.py

### Test File
* pick_your_letters_test.py

### Other File
* word.txt

## Progress
* ✓ - Finished
* O - In progess
* ? - Have problem
* blank - Not started

Section | State
:----: |:----:
Basic Logic |   ✓
Game Loop| ✓
Build easy AI | ✓
Build medium AI | ✓
Build hard AI | ✓
Corner cases check | ✓

## Overview of work accomplished
* This is a pick your letter game. You can play with a hard AI. The first side who successfully get a word from the dictionary is the winner. The logic is like:
* 
    ````
        Welcome to the game!
        Enter a number between 3 - 10 to be length of the word you are going to guess:
        3
        The length of the word is 3

        Try to get the words with 3 letters
        Initializing words pool......
        Game Start
        ---------------------------------------------------------------------
        Computers' turn

        Computer's current hand is: 

        ['d', 'm', 'n']
        Computer took v from DISCARD PILE
        Computer put n into DISCARD PILE
        Computer's current hand is:
        ['d', 'm', 'v']
        ---------------------------------------------------------------------
        Your turn

        Your word list is:
        ['q', 'y', 't']
        Pick 'n' from DISCARD PILE or reveal another letter from MAIN PILE
        Input 'D/d' to pick it from DISCARD PILE. Input 'M/m' to pick another letter from MAIN PILE: 
        1
        Invalid input! Type 'D/d' or 'M/m' 

        Input 'D/d' to pick it from DISCARD PILE. Input 'M/m' to pick another letter from MAIN PILE: 
        d
        You get a letter n from DISCARD PILE
        Input the index of the letter to be replaced, from 0 - 2
        m
        Invalid Input! Please make sure that your input is an integer between 0 - 2 ! 

        Input the index of the letter to be replaced, from 0 - 2
        1
        Your word list is: 
         ['q', 'n', 't']
        ----------------------------------------------------------------
        Game End! Computer Wins!! Its word is dmv .
    ````
* After getting into the system, the functions are different for each group.
