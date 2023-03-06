# Pick_your_letter_game
 
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
* This is a pick your letter game. You can play with a hard AI. The first side who successfully get a word from the dictionary is the winner. The logic is shown in the last section.
* The AI is stupid in the first version, it only stick to a single word for the whole game. After upgrading it for several times, it will search the best word every time so it is almost impossible to defeat it when the length of the target word is large.


## Challenges
* The design of AI is pretty challenging. I built a fair enough strategy for the AI:
* ````

  1. If the current word is a dictionary word, AI wins (exit).
  2. Compute the similarity between each dict word and current word:
     - wasp and swap has a similarity = 0
     - swap and swan has a similarity = 1
  3. Pick the letter if this target is better than the current target.
  4. else do not pick the letter and pass.
  ````
* As we can see, this is a method like BFS.

## Game Demo
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
