def main():
    book_text = read_book("books/frankenstein.txt")
    #print(book_text)
    word_count = count_words(book_text)
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



#if __name__ == "__main__":
main()