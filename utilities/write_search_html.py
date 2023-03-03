import requests
from bs4 import BeautifulSoup
from icecream import ic

url = "https://www.rent.com.au/properties/perth-wa-6000"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers)
# ic(response)
soup = BeautifulSoup(response.content, "html.parser")
# ic(soup)
class_name = "property-cell -normal"
property_listings = soup.find_all("article", class_=class_name)
# Write the contents of the soup object to a file
with open(f"rent_perth_{class_name}.html", "w", encoding="utf-8") as f:
    for listing in property_listings:
        f.write(listing.prettify())
        f.write('==============================================\n')
        f.write('==============================================\n')
