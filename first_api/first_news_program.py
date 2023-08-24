import requests

api_key = "a10e4275c28148379b16fe17441ccd9b"


def news_func():
    main_url = "https://newsapi.org/v2/top-headlines?country=bg&apiKey=" + api_key

    news = requests.get(main_url).json()
    articles = news["articles"]
    news_articles_titles = []
    news_articles_links = []
    news_articles_authors = []

    for article in articles:
        news_articles_titles.append(article["title"])
        news_articles_links.append(article["url"])
        news_articles_authors.append(article["author"])

    for index in range(len(news_articles_titles)):
        print(f"{index + 1}: {news_articles_titles[index]} - {news_articles_authors[index]}")
        print(f"LINK: {news_articles_links[index]}")


news_func()
