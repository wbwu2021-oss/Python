```python
themes={}

base_path=os.path.dirname(__file__)
file_path=os.path.join(base_path,'  ', 'data', 'word.txt')

if os.path.exists(file_path):
     with open(file_path, 'r')as f:
         for line in f:
            parts=line.strip().split(',')   

            theme=parts[0]
            words=parts[1:]
                 
            if theme not in themes:
                themes[theme]=[]
            themes[theme].append(word)
                 
 return themes.


Themes = load_words()


def get_word_from_theme(choice):
    keys = list(Themes.keys())

    try:
        index = int(choice) - 1
        if index < 0 or index >= len(keys):
            return None

        theme = keys[index]
        return random.choice(Themes[theme]).upper()

    except:
        return None

