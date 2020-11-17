import sys

import requests
import bs4

# get the URL that the user passed, or default to server side rendered page
try:
    url = sys.argv[1]
except IndexError:
    url = "https://okayweather.pythonanywhere.com/server_side_rendered"

# request and parse
response = requests.get(url)
parser = bs4.BeautifulSoup(response.text, "html.parser")

# select a tag that looks like <p class="name">...
name_and_location = parser.select("p.name")

# select a tag that looks like <p class="temperature">...
temperature = parser.select("p.temperature")

# print the text of those nodes
print(name_and_location[0].text.strip())
print(temperature[0].text.strip())
