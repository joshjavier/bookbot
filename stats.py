def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    count = {}
    for char in list(text):
        normalized_char = char.lower()
        if normalized_char in count:
            count[normalized_char] += 1
        else:
            count[normalized_char] =  1
    return count

def get_sorted_list(char_num_dict):
    result = []
    for char in char_num_dict:
        item = {"char": char, "num": char_num_dict[char]}
        result.append(item)

    def sort_on(item):
        return item["num"]

    result.sort(reverse=True, key=sort_on)
    return result
