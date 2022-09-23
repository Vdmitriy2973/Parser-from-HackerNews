from bs4 import BeautifulSoup as BS
import requests
import translators as ts


for j in range(1,5):
    url = f"https://news.ycombinator.com/news?p={j}"
    r = requests.get(url)
    soup = BS(r.content, "lxml")
    tr = soup.find_all("tr", class_="athing")

    for i in tr:
        print(ts.google(i.text, to_language="ru"))
        td = i.find_all("td")
        href = td[2].find("a").attrs["href"]
        print(href, "\n")