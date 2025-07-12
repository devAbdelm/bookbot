def count_words(string):
    return len(string.split())

def count_chars(string):
    lower_string = string.lower()
    chars = {}
    for char in lower_string:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sorted_dictionaries(dictionary):
    
    def sort_key(item):
        return item["num"]
    
    dictionaries = []
    
    for key in dictionary.keys():
        new_dictionary = {}
        new_dictionary["char"],new_dictionary["num"] = key, dictionary.get(key)
        dictionaries.append(new_dictionary)

    dictionaries.sort(reverse=True, key=sort_key)
    return dictionaries