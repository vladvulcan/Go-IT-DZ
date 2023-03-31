import re


def replace_spam_words(text, spam_words):
    not_spam = text
    for word in spam_words:
        spam = re.search(word,text,flags=re.IGNORECASE)
        asterisks = ''
        if spam:
            for i in spam[0]:
                asterisks += '*'
            not_spam = re.sub(spam[0],asterisks,not_spam,flags=re.IGNORECASE) 
        else: pass
    return not_spam