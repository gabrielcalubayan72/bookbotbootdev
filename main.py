import sys

def main():
    PATH = "books/frankenstein.txt"
    words = get_book_text(PATH)
    print(f"--- Begin report of {PATH} ---")
    print(f"{get_num_words(words)} words found in document")

    for dict in sort_dict(words):
        print(f"The '{dict['char']}' character was found {dict['count']} times")

    print(f"--- End report of {PATH} ---")

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

def convert_dict(char_dict):
    char_dict_list = []
    for char in char_dict:
        char_dict_list.append({"char": char, "count": char_dict[char]})
    return char_dict_list

def sort_dict(char_dict):
    converted = convert_dict(count_characters(char_dict))
    converted.sort(reverse=True, key=sort_on)
    return converted




def get_num_words(text: str):
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str, int]:
    lowered_string = text.lower()
    character_dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in lowered_string:
        if char in alphabet:
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
