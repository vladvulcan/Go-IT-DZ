import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z][\w\.]{1,}@[a-z]+\.[a-z]{2,}", text)
    return result