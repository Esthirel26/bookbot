def get_num_words(f):
    # get the number of words
    x = 0
    with open(f) as txt: #open a file at a specific path
        file_contents = txt.read() # read a file and stock it in file_contents
        words = file_contents.split()

        for word in words: #count the number of word
            x += 1
        
        return x

def get_num_character(f):
    #get the number of any character
    dict_character = {}
    with open(f) as txt: #open a file at a specific path
        file_contents = txt.read() # read a file and stock it in file_contents
        lower_txt = file_contents.lower() # lower every character to avoid doublon
        for character in lower_txt: # iterate throw every character of all the word
            dict_character[character] = dict_character.get(character, 0) + 1 
            # if the character is not in the dictionnaries creat an entry, if it is increment by 1
    
    return dict_character

def sort_on(dict):
    # This returns the count value for sorting
    return dict["count"]  # This assumes each dict has a "count" key

def list_dict(char_dict):
    # Convert dictionary to list of dictionaries
    char_list = []
    char_dict = get_num_character(char_dict) # get the number of character
    for char, count in char_dict.items(): # transforme the dictionnaries into a list
        char_list.append({"char": char, "count": count})
    
    # Sort the list by count, highest first
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list