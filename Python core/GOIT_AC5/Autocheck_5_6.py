def is_spam_words(text, spam_words, space_around=False):
    if space_around:
        for i in spam_words:
            if f" {i}" in text.lower():
                x = True
            elif f" {i}." in text.lower():
                 x = True
            else: x = False
        return x
    else:
        for i in spam_words:
            return i in text.lower()