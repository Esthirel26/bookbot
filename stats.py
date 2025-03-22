def get_num_words(f):
    x = 0
    with open(f) as txt:
        file_contents = txt.read()
        words = file_contents.split()

        for word in words:
            x += 1
        
        return x


