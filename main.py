def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count_dict = get_letter_count(text)
    letter_count_list = convert_dict_to_list(letter_count_dict)
    letter_count_list.sort(reverse=True, key=sort_on)
    print_report(book_path, num_words, letter_count_list)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    words = text.lower()
    letter_count = {}
    for letter in words:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def convert_dict_to_list(dict):
    list_of_dicts = []
    for item in dict:
        item_dict = {
            'character': item,
            'num': dict[item],
        }
        list_of_dicts.append(item_dict)
    return list_of_dicts

def sort_on(dict):
    return dict['num']

def print_report(book_path, num_words, letter_count_list):
    print(f'--- Begin report of {book_path} ---\n{num_words} words found in the document\n')
    for char_dict in letter_count_list:
        print(f"The '{char_dict['character']}' character was found {char_dict['num']} times")
    print('--- End report ---')

main()