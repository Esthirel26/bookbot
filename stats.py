def get_num_words(f):
    x = 0
    with open(f) as txt:
        file_contents = txt.read()
        words = file_contents.split()

        for word in words:
            x += 1
        
        return x

def get_num_character(f):
    dict_character = {}
    with open(f) as txt:
        file_contents = txt.read()
        lower_txt = file_contents.lower()
        for character in lower_txt:
            dict_character[character] = dict_character.get(character, 0) + 1
    
    return dict_character
