```python

import random
"""
Word list with different themes
"""

# define the word list with different themes
Themes={"1":("animals", ["tiger", "zebra", "rabbit", "wolf","panda"]),
        "2":("food", ["bread", "pizza", "burger", "noodle"]),
        "3":("sport", ["soccer", "tennis", "bedminton", "surfing"，“skate"]}

def get_world_from_theme(choice):
"""
select a random word with a theme
"""
if choice in Themes:
    return random.choice(Themes[choice][1])
return None
```
