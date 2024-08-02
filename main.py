book_path = "books/frankenstein.txt"

def main():
    text = get_books(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    review(word_count, letter_sort(letter_count))


# Read books in path return text
def get_books(path):
    with open(path) as f:
        return f.read()

# Split text and return int of space split Strings
def count_words(text):
    words = text.split()
    return len(words)

# return dictionary of all letters in text and quantity
def count_letters(text):
    letter_dict = {}
    lowered = text.lower()
    for letter in lowered:
        if letter not in letter_dict:
            letter_dict.update({letter : 1})
        else: 
            letter_dict[letter] += 1
    return letter_dict       

# return dictionary sorted by Value desc
def letter_sort(letters_dict):
    sorted_letters_list= sorted(letters_dict.items(), key=lambda x:x[1], reverse= True)
    sorted_letters_dict = dict(sorted_letters_list)
    return sorted_letters_dict


def review(word_count, letter_count):
    print(f"--- Begin report of {book_path} ---")   
    print(f"{word_count} words were found")
    print("")
    
    letter_dict_list = list()
    letter_dict_list = letter_count.keys()

    for letter in letter_dict_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_count[letter]} times")
    print("--- End of report ---")
    


main()