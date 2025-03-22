import sys
from stats import get_num_words
from stats import list_dict


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    pwd = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pwd}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(pwd)} total words")
    print("--------- Character Count -------")
    
        # Print only alphabetic characters
    char_list = list_dict(pwd)
    for item in char_list:
         char = item["char"]
         if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {item['count']}")
        
    print("============= END ===============")

main()