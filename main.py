from stats import get_num_words
from stats import get_num_character

def main(): 
    print(f"{get_num_words("/home/dk/bootdevtuto/git/bookbot/books/frankenstein.txt")} words found in the document")
    print(get_num_character("/home/dk/bootdevtuto/git/bookbot/books/frankenstein.txt"))

main()