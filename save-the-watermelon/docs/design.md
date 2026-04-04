# design
##- Problem statement & target audience.
It is a terminal-based word-guessing game and suite for English learner. it helps to imporve vocabulary.

##- Game rules & win/lose conditions. 
6 slices watermelon in total. Each incorrect guess decrease one slice watermelon.The game is over when the slice becomes "0". Or the player win.
Select a random word from the list and hide 2 or 3 random letters, show as "_a_e". The player fill one letter on the "_".

##- Core features (must-have) vs stretch goals (nice-to-have). 
Core features: 1. Randomly select a word from the list;
               2. Hide 2 or 3 random letters in a word and hide them;
               3. Input one letter one time on the "_";
               4. Decrease one slice when the player input a incorrect letter.
               5. 6 slices in total, and figure out the whole word before the number of the slice is zero.
stretch goals: set the words by themes, and the player can choose a suitable theme.

##- Basic flow diagram or bullet-flow (start → loop guess → win/lose).
1:Select a theme, 2: Randomly hide 2 or 3 letters, 3: Let the player input,
4: check the answer "right" or "wrong", 5: If "right", show a new word and show "win", 6: If "wrong", decrease a slice, 7: If the slice="0", show"lose". 8. Replay or not.

##- Data design: 
- How you store the word---- "secret_word"
-  revealed letters----"display list",
-  guessed letters----"guessed_letter",
-  remaining slices---"slice_left".
