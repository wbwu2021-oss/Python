"""
import the themes from src.words and import the hiding, checking coding from src.logic
"""
from src.words import Themes, get_word_from_theme
from src.logic import mask_random_letters, check_guess, is_word_complete

def get_valid_input(guessed_letters):
  while True:
    guess=input("guess a missing letter:").strip().lower()
    if len(guess)!=1 or not guess.isalpha():
        print("invalid input!please enter a single letter")
    elif guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different one!")
    else:
        return guess


def display_game_status(display_list,slices,guessed_letters):
    print("\nword:"," ".join(display_list))
    print("Watermelon slices left:", slices)
    print("guessed letters:"," ".join(guessed_letters) if guessed_letters else "None")

def play_game():
    print("\nWELCOME TO SAVE THE WATERMELON!")
    print("-" * 30)

    if not Themes:
        print("the words are not available")
        return


    print("choose a theme:")
    theme_names=list(Themes.keys())

    for i, theme in enumerate (theme_names,start=1):
        print(f"{i}.{theme.title()}")

    choice=input("enter number(1-3):").strip()
    secret_word=get_word_from_theme(choice)

    if not secret_word:
        print("Invalid choice. Selecting 'Animals' by default.")
        secret_word = get_word_from_theme("1")


# default setting

    display_list, hidden_indices=mask_random_letters(secret_word)
    slices=6
    guessed_letters = []

# guess the letter

    while slices >0 and not is_word_complete(display_list):
        display_game_status(display_list,slices,guessed_letters)

        guess = get_valid_input(guessed_letters)
        guessed_letters.append(guess)

        if check_guess(guess, secret_word, display_list, hidden_indices):
            print("good job")
        else:
            slices=slices-1
            print("please try again")

    print("\nFinal word:"," ".join(display_list))
    if is_word_complete(display_list):
        print("win")
    else:
        print("lose")



def main():
    while True:
        play_game()
        again=input("\n Do you want to replay? (Y/N):").strip().upper()

        if again!="Y":
            print("welcome back!")
            break

if __name__=="__main__":
  main()


