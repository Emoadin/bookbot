def main():
    book_text = read_book("books/frankenstein.txt")
    #print(book_text)
    word_count = count_words(book_text)
    char_count = count_char(book_text)
    print(char_count)
    print(word_count)

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_char(text):
    text_set = set()
    text_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        text_set.add(char)
    text_set.remove(' ')
    for char in text_set:
        text_dict.update({char: 0})
    for char in lower_text:
        if char in text_dict:
            text_dict[char] += 1
        

    return text_dict


#if __name__ == "__main__":
main()