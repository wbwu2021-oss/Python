# hiding 2 or 3 letters and check the answer

```python
import random

def mask_random_letters(word):
    word_list=list(word)
    num_to_hide=random.randint(2,3)
  
    hidden_indices=random.sample(range(len(word)), num_to_hide)
  
  display_list=[]
  for i in range(len(word)):
      if i in hidden_indices:
          display_list.append("_")
      else:
          display_list.append(word[i])

  return display_list, hidden_indices

def check_guess(guess, secret_word, display_list, hidden_indices):
     found=False

    for i in hidden_indices:
      if secret_word[i]==guess:
         display_list[i]=guess
         found=True
    return found
```

