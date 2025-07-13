def count_words(content):
    words = content.split()
    return len(words)

def count_characters(content):
    low_content = content.lower()
    characters = {}
    for a_char in low_content[:]:
        if a_char not in characters:
            characters[a_char] = 1
        else:
            characters[a_char] += 1
    return characters

def sort_by_num(items):
    return items["num"]

def count_characters_sorted(content):
    char_dict = count_characters(content)
    list_dict = []
    for key in char_dict:
        list_dict.append({"char":key,"num":char_dict[key]})

    list_dict.sort(reverse=True,key=sort_by_num)
    return list_dict