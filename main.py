import sys

def main():
    PATH = "books/frankenstein.txt"
    words = get_book_text(PATH)
    print(f"The book is {get_num_words(words)} words!")
    print(f"Character dictionary: {count_characters(words)}")

def get_num_words(text: str):
    words = text.split()
    return len(words)

def count_characters(text: str):
    lowered_string = text.lower()
    character_dict = {}

    for char in lowered_string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

if __name__ == '__main__':
    sys.exit(main()) 
