import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from icecream import ic

url = "https://www.realestate.com.au/rent/in-perth+-+greater+region,+wa/list-1"
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
ic(soup)

property_listings = soup.find_all("article", class_="resultBody")
ic(property_listings)

for listing in property_listings:
    # Extract relevant information from each listing
    address = listing.find("a", class_="detailsLink").text.strip()
    price = listing.find("span", class_="property-price").text.strip()
    beds = listing.find("span", class_="general-features").find_all("span")[0].text.strip()
    baths = listing.find("span", class_="general-features").find_all("span")[1].text.strip()
    cars = listing.find("span", class_="general-features").find_all("span")[2].text.strip()
    
    print(f"Address: {address}\nPrice: {price}\nBeds: {beds}\nBaths: {baths}\nCars: {cars}\n")
