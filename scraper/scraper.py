import requests

from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Oh no! Something went wrong. Maybe check your internet connection? More details:")
    print(e)
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    if response.status_code == 200:
        # p_tags = soup.find_all('p')
        # first_h1 = soup.find('h1')
        # # print(p_tags)
        # print(first_h1)

        articles = soup.select('article.product_pod')
        print(f"Number of books: {len(articles)}")

        p_prices = soup.select('article.product_pod div.product_price p.price_color')
        prices = [float(price.text[2:]) for price in p_prices]
        print(f"Average price: {round(sum(prices) / len(prices), 2)}")

        product_titles = soup.select('article.product_pod h3 a')
        product_titles = [product_title['title'] for product_title in product_titles]
        titles_with_prices = {}
        for title, price in zip(product_titles, prices):
            titles_with_prices[title] = price

        print(titles_with_prices)
        print(f"Most expensive book: {max(titles_with_prices, key=titles_with_prices.get)}")

    else:
        print(f"Unexpected response: {soup.prettify()}")




