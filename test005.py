import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.google.com/maps/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90")
soup = BeautifulSoup(result.text, "html.parser")
pagination = soup.find("div", {"class":"siAUzd-neVct section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc siAUzd-neVct-Q3DXx-BvBYQ"})
pages = pagination.find_all('a')

print(pages)