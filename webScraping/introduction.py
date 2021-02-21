import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://madyfit.com/collections/all-products/products/bandas-de-resistencia?variant=36832771670176")

soup = BeautifulSoup(html.read(), "html.parser")
button = soup.find_all("button", {"class" : "product-form--add-to-cart" })

# print(button)
# print(soup.encode("utf-8"))
