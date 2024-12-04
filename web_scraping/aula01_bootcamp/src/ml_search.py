import requests
from bs4 import BeautifulSoup

keyword = "PS5"

url = f"https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    search_result = soup.find_all("div", class_="ui-search-result")

    data = []

    for result in search_result:
        link = result.find("a", class_="ui-search-link").get("href")
        title = result.find("h2", class_="ui-search-item__title").text
        price = result.find("span", class_="price-tag-fraction").text
        brand = result.find("span", class_="ui-search-item__group__element").text

        data.append({"link": link, "title": title, "price": price, "brand": brand})

    print(data)
else:
    print(f"Error: {response.status_code}")
