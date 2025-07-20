def get_word_count(text):
    words = text.split()
    return len(words)


def get_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_dict(dict):
    list_of_new_dicts = []
    new_dict = {}
    # create new list containing dictionaries of new key/value pairs char:char and count:count
    for char, value in dict.items():
        if char.isalpha():
            new_dict = {"char": char, "count": value}
            list_of_new_dicts.append(new_dict)
    # sort list by count from highest to lowest (requires reverse language)
    sorted_by_count = sorted(list_of_new_dicts, key=lambda x: x["count"], reverse=True)
    return sorted_by_count