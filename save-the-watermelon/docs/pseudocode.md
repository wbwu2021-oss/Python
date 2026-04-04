# progression 2

## FUNCTION main_game_loop
Select a theme
Display available theme: food, sport, animal
choice ← prompt_for_theme
word_list ← load_words

secret ← select_secret_word(word_list)
guessed ← ∅
slices ← MAX_SLICES==6

WHILE slices > 0 AND NOT is_win(secret, guessed)
    DISPLAY render_state(secret, guessed)
    
    guess ← prompt_for_letter()
    
IF guess already in guessed THEN
      DISPLAY "Already guessed"
      CONTINUE
ENDIF
ADD guess TO guessed

IF guess IN secret THEN
      DISPLAY "Nice!"
ELSE
      slices ← slices - 1
      DISPLAY "Sliced! Remaining: " + slices
ENDIF
ENDWHILE

IF is_win(secret, guessed) 
    DISPLAY "You saved the watermelon!"
ELSE 
     DISPLAY "Oh no! The melon was sliced."
END FUNCTION
