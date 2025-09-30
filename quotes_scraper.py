import requests

from bs4 import BeautifulSoup

from collections import Counter

url = "http://quotes.toscrape.com/page/1/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
    quotes_data.append({"text": text, "author": author, "tags": tags})

total_quotes = len(quotes_data)
print("Total quotes:", total_quotes)

unique_authors = {q["author"] for q in quotes_data}
print("Unique authors:", len(unique_authors))

author_counts = Counter([q["author"] for q in quotes_data])
top_author, top_count = author_counts.most_common(1)[0]
print("Author with most quotes:", top_author, f"({top_count})")

quotes_with_is = sum(1 for q in quotes_data if "is" in q["text"].lower())
print("Quotes containing 'is':", quotes_with_is)

all_tags = [tag for q in quotes_data for tag in q["tags"]]
tag_counts = Counter(all_tags)
print("Tags frequency:")

for tag, count in tag_counts.most_common():
    print(f"  {tag}: {count}")
