```python
"""
import the themes from src.words and import the hiding, checking coding from src.logic
"""
from src.words import Themes, get_word_from_theme
from src.logic import mask_random_letters, check_guess
def play_game():
  print("select a theme:")
  for key in Themes.items():
    print(f"{key}.{value[0]}")
choice=input("enter number(1,2,3):")
secret_word=get_word_from_theme(choice)

"""
default setting
"""
display_list, hidden_indices=mask_random_letters(secret_word)
slices=6

"""
guess the letter
"""
while slice>0
 print(f"\nword:{''.join(display_list)}")

 if check_guess(guess, secret_word, display_list, hidden_indices):
   print("good job")
 else:
   slices=slices-1
   print("please try again")

if __name__=="__main__":
  while True:
    play_game()
    if input ("play again?(y/n):").lower()!="y":
      print("Thanks for playing")
      break






