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
# ic(property_listings[1])


for listing in property_listings:
    # Extract relevant information from each listing
    address = listing.find('h2', {'class': 'address'}).get_text().strip()
    beds = listing.find('span', {'class': 'icon-beds -icon-block'}).find_next('span').get_text().strip()
    baths = listing.find('span', {'class': 'icon-baths -icon-block'}).find_next('span').get_text().strip()
    price = listing.find('span', {'class': 'price'}).get_text().strip()
    parking_spaces = listing.find('span', {'class': 'icon-cars -icon-block'}).find_next('span').get_text().strip()
    # latitude = soup.find('meta', {'property': 'place:location:latitude'})['content']
    # longitude = soup.find('meta', {'property': 'place:location:longitude'})['content']

    ic(address)
    ic(beds)
    ic(baths)
    ic(price)
    ic(parking_spaces)
    # ic(latitude)
    # ic(longitude)