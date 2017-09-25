from bs4 import BeautifulSoup

import requests

url = "https://maroof.sa/BusinessType/BusinessesByTypeList?bid=23&sortProperty=BestRating&DESC=True"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print link
    # print(link.get('href'))