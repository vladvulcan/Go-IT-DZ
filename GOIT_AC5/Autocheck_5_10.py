import re


def find_word(text, word):
    dict = {}
    search = re.findall(word, text)
    match = re.search(word, text)
    if len(search) != 0:
        indexes = match.span()
        dict['result'] = True
        dict['first_index'] = indexes[0]
        dict ['last_index'] = indexes[1]
        dict['search_string'] = word
        dict['string'] = text
    else:
        dict['result'] = False
        dict['first_index'] = match
        dict ['last_index'] = match
        dict['search_string'] = word
        dict['string'] = text
    return dict