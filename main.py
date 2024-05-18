def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    #print(book_text)
    word_count = count_words(book_text)
    char_count = count_char(book_text)
    #print(char_count)
    print(f"--- Begin Report of {book_path} ---")
    print(f"There were {word_count} words found in the document.")
    dict_list = convert(char_count)
    dict_list.sort(reverse=True, key=sort_on)
    for char in dict_list:
        if char['char'].isalpha():
            print(f"The '{char['char']}' character was found {char['num']} times.")
    print(f"--- End of Report ---")
    #print(dict_list)
    

    

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

def convert(dict):
    dict_list = []  
    for k, v in dict.items():
       new_dict = {"char": k, "num": v}
       dict_list.append(new_dict)
    return dict_list

def sort_on(dict):
    return dict["num"]  






#if __name__ == "__main__":
main()