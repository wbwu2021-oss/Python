```python
import random
import os
"""loading words from the data/words.txt
"""
def load_words():
        themes={}
        base_path=os.path.dirname(__file__)
        file_path=os.path.join(base_path,'  ', 'data', 'word.txt')

try:
        with open(file_path, 'r')as f:
                for line in f:
                        theme, word=line, strip(),split(',')
                        if theme not in [theme]=[]
                        themes[theme].append(word)
return themes.


