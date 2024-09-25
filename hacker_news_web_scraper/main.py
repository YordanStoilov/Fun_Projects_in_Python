import requests
from bs4 import BeautifulSoup


def filter_out_articles(links_list, subtext_string):
    articles = []
    for idx, item in enumerate(links_list):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext_string[idx].select(".score")
        if vote:
            points = int(vote[idx].getText().replace(" points", ""))
            if points >= 100:
                articles.append({"Title": title, "Points": points, "Link": href})
    return articles


address = "https://news.ycombinator.com"

response = requests.get(address)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.select(".titleline")
subtext = soup.select(".score")

print(filter_out_articles(links, subtext))
