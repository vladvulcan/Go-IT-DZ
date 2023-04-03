def real_len(text):
    new_text =''
    for i in text:
        if i not in [ '\n', '\f', '\r', '\t', '\v']:
            new_text += i
    return len(new_text)