import requests
from bs4 import BeautifulSoup

url = "https://www.rent.com.au/properties/perth-wa-6000"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Write the contents of the soup object to a file
with open("rent_perth.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
