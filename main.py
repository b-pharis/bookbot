def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_characters(text)
    letters_list = chars_to_list(letter_count)
    letters_list.sort()
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    count_by_letter(letters_list)
    print("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    lowered_text = text.lower()
    characters = {}
    for character in lowered_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
        
    return characters

def chars_to_list(letter_count):
    char_list = []
    for dict in letter_count:
        if dict.isalpha() == True:
            char_list.append((dict, letter_count[dict]))
    return char_list

def count_by_letter(letters_list):
    for char, count in letters_list:
        print(f"The '{char}' character was found {count} times")
main()