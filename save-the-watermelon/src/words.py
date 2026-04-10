import os
import random

def load_words():
    themes={}

    base_path=os.path.dirname(__file__)
    file_path=os.path.join(base_path,'..', 'data', 'words.txt')
    file_path=os.path.abspath(file_path)

    if not os.path.exists(file_path):
        return themes

    with open(file_path,'r') as f:
        for line in f:
            parts=[item.strip() for item in line.strip().split(',')]

            if len(parts)!=2:
                continue

            theme=parts[0]
            word=parts[1]
                 
            if theme not in themes:
                 themes[theme]=[]
            themes[theme].append(word)
                 
    return themes


Themes = load_words()


def get_word_from_theme(choice):
    keys = list(Themes.keys())

    try:
        index = int(choice) - 1
        if index < 0 or index >= len(keys):
            return None

        theme = keys[index]
        return random.choice(Themes[theme]).lower()

    except ValueError:
        return None

