def get_books_text(f):
    x = 0
    with open(f) as txt:
        file_contents = txt.read()
        words = file_contents.split()

        for word in words:
            x += 1
        
        return x

def main(): 
    print(f"{get_books_text("/home/dk/bootdevtuto/git/bookbot/books/frankenstein.txt")} words found in the document")


main()