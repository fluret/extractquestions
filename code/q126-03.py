def character_counter(text):
    characters_list = list(text)
    char_count = {}
    for x in characters_list:
        if x in char_count.keys():
            char_count[x] += 1
        else:
            char_count[x] = 1
    return char_count


def dict_viewer(dictionary):
    for x, y in dictionary.items():
        print(f"{x},{y}")


text = input("> ")
dict_viewer(character_counter(text))
