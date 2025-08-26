def count_words(str):
    return len(str.split())


def count_chars(str):
    dict = {}

    for char in str:
        lowercase_char = char.lower()
        current = dict.get(lowercase_char, -1)
        if current == -1:
            dict[lowercase_char] = 1
        else:
            dict[lowercase_char] = current + 1

    return create_sorted_dict_list(dict)


def sort_on(items):
    return items["num"]


def create_sorted_dict_list(dict):
    list = []

    for k, v in dict.items():
        if k.isalpha():
            list.append({"char": k, "num": v})

    list.sort(reverse=True, key=sort_on)

    return list
