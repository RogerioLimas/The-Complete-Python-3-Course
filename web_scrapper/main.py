import requests
from bs4 import BeautifulSoup
import os

# search = input("Enter search term: ")

params = {"q": "pizza"}
r = requests.get('http://www.bing.com/search', params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    a = item.find("a")
    item_text = a.text
    item_href = a.attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
    