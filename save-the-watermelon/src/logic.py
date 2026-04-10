
import random

def mask_random_letters(word):
    """
    hide 2 or 3 letters
    """
    word = word.lower()
    word_list=list(word)
# avoid the length of the secret word beyond the word

    num_to_hide=min(random.randint(2,3), len(word))
  
    hidden_indices=random.sample(range(len(word)), num_to_hide)
  
    display_list=[]
    for i in range(len(word)):
        if i in hidden_indices:
            display_list.append("_")
        else:
            display_list.append(word_list[i])

    return display_list, hidden_indices
"""
check whether guessd letter is right or wrong.
"""
def check_guess(guess, secret_word, display_list, hidden_indices):
    guess = guess.lower()
    secret_word = secret_word.lower()

    found=False

    for i in hidden_indices:
        if secret_word[i]==guess and display_list[i]=="_":
            display_list[i]=guess
            found=True
    return found

def is_word_complete(display_list):
    return"_" not in display_list


