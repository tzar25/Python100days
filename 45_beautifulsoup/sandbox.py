from bs4 import BeautifulSoup
import requests

# with open("website.html") as website:
#     data_raw = website.read()
#
# soup = BeautifulSoup(data_raw, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# all_anchors = soup.find_all(name="a")
# print(all_anchors)
# for tag in all_anchors:
#     print(tag.get_text())
#     print(tag["href"])
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# """My 1st solution to get max score"""
# max_score = 0
# max_id = None
# for entry in soup.find_all(name="span", class_="score"):
#     score = int(entry.get_text().split()[0])
#     if score > max_score:
#         max_score = score
#         max_id = entry["id"]
#
# print(soup.find(name="tr", id=max_id[6:]).select(selector="a")[1].get_text())

# """My final solution"""
articles = [[article.find(name="a").text, article.find(name="a")["href"]] for article in soup.find_all(name="span", class_="titleline")]

scores = [int(entry.text.split()[0]) for entry in soup.find_all(name="span", class_="score")]

articles = zip(articles, scores)
max_score = 0
top_article = None
for article in articles:
    if article[1] > max_score:
        max_score = article[1]
        top_article = article
print(top_article[0][0])
print(top_article[0][1])
print(f"Score: {top_article[1]}")
