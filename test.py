import requests
from bs4 import BeautifulSoup
from icecream import ic
import re

url = "https://www.rent.com.au/properties/perth-wa-6000?page=13"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

class_name = "property-cell -normal"
property_listings = soup.find_all("article", class_=class_name)

# Extract metadata for the first page
metadata = {
    'total_properties': 0,
    'bedroom_count': {},
    'average_price': 0,
    'parking_count': {}
}

total_price = 0
total_properties = 0
bedroom_count = {}
parking_count = {}

for listing in property_listings:
    # Extract relevant information from each listing
    address = listing.find('h2', {'class': 'address'}).get_text().strip()
    beds = listing.find('span', {'class': 'icon-beds -icon-block'}).find_next('span').get_text().strip()
    baths = listing.find('span', {'class': 'icon-baths -icon-block'}).find_next('span').get_text().strip()
    price = listing.find('span', {'class': 'price'}).get_text().strip()
    parking_spaces = listing.find('span', {'class': 'icon-cars -icon-block'}).find_next('span').get_text().strip()
    
    # Update metadata
    try:
        price_float = float(re.sub(r'[^\d\.]+', '', price))
        if price_float > 5000.0:
            # if the price is above some threshold, check to see if they used a price range with some regex magic
            prices = re.findall(r'\d+(?:,\d+)*(?:\.\d+)?|\d+(?:\.\d+)?', price)
            prices = [re.sub(r'[^\d\.]+', '', x) for x in prices]
            prices = [float(price) for price in prices]
            price_float = sum(prices) / len(prices)
        ic(price_float)
        total_price += price_float
        total_properties += 1
        bedroom_count[beds] = bedroom_count.get(beds, 0) + 1
        parking_count[parking_spaces] = parking_count.get(parking_spaces, 0) + 1
    except ValueError:
        print('price not available, excluding from metadata aggregation') 

metadata['total_properties'] = total_properties
metadata['bedroom_count'] = bedroom_count
metadata['average_price'] = total_price / total_properties
metadata['parking_count'] = parking_count

ic(metadata)
