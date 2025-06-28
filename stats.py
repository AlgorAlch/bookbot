from functools import reduce

def nr_of_words(text):
    words = text.split()
    return len(words)

def nr_of_chars(text):
    chars = list(text)

    def add_char_to_dict(dic, char):
        if char.lower() in dic:
            dic[char.lower()] += 1
        else:
            dic[char.lower()] = 1
        return dic
    
    chars_dict = reduce(add_char_to_dict, chars, {})
    
    return chars_dict


def sort_dict(dict_to_sort):
    d = {key:value for key, value in dict_to_sort.items() if key.isalpha()}
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
