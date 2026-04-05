```python
"""
hiding 2 or 3 letters and check the answer
"""
import random
def mask_random_letters(word):
  word_list=list(word)
  num_to_hide=random.randint(2,3)
  hidden_indices=random.sample(range(len(word))), num_to_hide)
  
  display_list=[]
  for i in range(len(word)):
    if i in hidden_indices:
      display_list.append("_")
    else:
      display_list.append(word[i])

  return display_list, hidden_indices

def check-guess(guess, secret_word, displau_list, hidden_indices):
    for i in hidden_indices:
      if secret_word[i]==guess;
         display-list[i]=guess
         found=True
    return found
```

