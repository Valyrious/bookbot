def main():
    book_path = "books/frankenstein.txt"
    text = get_books(book_path)
    # print(text)
    word_count = count_words(text)
    # print(word_count)
    count_letters(text)

def get_books(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict = {}
    lowered = text.lower()
    for letter in lowered:
        if letter not in letter_dict:
            letter_dict.update({letter : 1})
        else: 
            letter_dict[letter] += 1
    print(letter_dict)           

main()