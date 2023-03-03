import requests
from bs4 import BeautifulSoup
from icecream import ic

url_template = "https://www.rent.com.au/properties/perth-wa-6000?page=%d"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Initialize variables to store metadata
total_properties = len(property_listings)
bedrooms = {}
parking_spaces = {}
total_price = 0

for page_num in range(1, 11): # Update the range based on the number of pages
    url = url_template % page_num
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    class_name = "property-cell -normal"
    property_listings = soup.find_all("article", class_=class_name)

    for listing in property_listings:
        # Extract relevant information from each listing
        address = listing.find('h2', {'class': 'address'}).get_text().strip()
        beds = listing.find('span', {'class': 'icon-beds -icon-block'}).find_next('span').get_text().strip()
        baths = listing.find('span', {'class': 'icon-baths -icon-block'}).find_next('span').get_text().strip()
        price = listing.find('span', {'class': 'price'}).get_text().strip()
        parking_spaces = listing.find('span', {'class': 'icon-cars -icon-block'}).find_next('span').get_text().strip()

        ic(address)
        ic(beds)
        ic(baths)
        ic(price)
        ic(parking_spaces)

        num_properties += 1
        if beds == 1:
            num_1_beds += 1
