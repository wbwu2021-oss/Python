```python
"""
import the themes from src.words and import the hiding, checking coding from src.logic
"""
from src.words import Themes, get_word_from_theme
from src.logic import mask_random_letters, check_guess
def get_valid_input(guessed_letters):
  while True:
    guess=input("guess a missing letter:").upper()
    if len(guess)!=1 or not guess.isalpha():
      print("invalid input!please enter a single letter")
    elif guess in guessed_letters:
      print(f"You already guessed '{guess}'. Try a different one!")
    else:
      return guess


def play_game():
  print("\nWELCOME TO SAVE THE WATERMELON!")
    print("-" * 30)

  print("choose a theme:")
  for key, value in Themes.items():
    print(f"{key}.{value[0]}")

  choice=input("enter number(1-3):")
  secret_word=get_word_from_theme(choice)

  if not secret_word:
        print("Invalid choice. Selecting 'Animals' by default.")
        secret_word = get_word_from_theme("1")

"""
default setting
"""
  display_list, hidden_indices=mask_random_letters(secret_word)
  slices=6
  guessed_letters = set()

"""
guess the letter
"""
while slices >0 and "_" in display_list:
    print(f"\nword:{''.join(display_list)}")

    guess = get_valid_input(guessed_letters)
    guessed_letters.add(guess)

    if check_guess(guess, secret_word, display_list, hidden_indices):
        print("good job")
    else:
        slices=slices-1
        print("please try again")

if "_" not in display_list:
        print(f"\nVICTORY! You saved the watermelon! Word: {secret_word}")
    else:
        print(f"\nGAME OVER! The melon was sliced. The word was: {secret_word}")


if __name__=="__main__":
  while True:
    play_game()
    if input ("play again?(y/n):").lower()!="y":
      print("Thanks for playing")
      break


