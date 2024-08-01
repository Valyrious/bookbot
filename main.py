letter_dict = dict()

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
    lowered_text = text.lower()
    words = lowered_text.split()
    for word in words:
        for letter in word:
            if letter not in letter_dict:
                letter_dict.update({letter : 1})
            else: 
                x = letter_dict[letter]
                letter_dict[letter] = x+1
    print(letter_dict)           

main()