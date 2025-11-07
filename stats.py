def word_count(text):
    words = text.split()
    return len(words)


def count_chars(text):
    convert_to_lowercase = text.lower()
    char_dict = {}
    for char in convert_to_lowercase:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(item):
    return item["num"]


def sorted_list_dict(char_dict):
    sorted_list = []
    for key, value in char_dict.items():
        if key.isalpha() == True:
            sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
