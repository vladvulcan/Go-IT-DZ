articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_articles_dict = []
    for article in articles_dict:
        if letter_case:
            title = article["title"]
            author = article["author"]
            if title.find(key)!= -1 or author.find(key)!= -1:
                new_articles_dict.append(article)                
            else:
                continue
        else:
            key = key.lower()
            title = article["title"].lower()
            author = article["author"].lower()
            if title.find(key)!= -1 or author.find(key)!= -1:
                new_articles_dict.append(article)                
            else:
                continue
    return new_articles_dict