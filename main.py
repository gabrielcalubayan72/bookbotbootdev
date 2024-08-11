import sys

def main():
    PATH = "books/frankenstein.txt"
    words = get_num_words(get_book_text(PATH))
    print(f"The book is {words} words!")

def get_num_words(text: str):
    words = text.split()
    return len(words)

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

if __name__ == '__main__':
    sys.exit(main()) 
