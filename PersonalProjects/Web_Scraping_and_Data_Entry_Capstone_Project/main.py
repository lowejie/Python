import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# -------------------------------
# PART 1: Web Scraping (ibilik.my)
# -------------------------------


# Target URL (Penang rental listings)
BASE_URL = "https://www.ibilik.my/rooms/penang"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(BASE_URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Initialize lists
room_links = []
room_prices = []
room_addresses = []

# TODO: update selectors after checking the ibilik.my HTML structure
listings = soup.select("div.home-list-pop")  

for listing in listings:
    # Link
    link_tag = listing.select_one("div.col-md-4 a")
    link = link_tag["href"] if link_tag else None
    if link and not link.startswith("http"):
        link = "https://www.ibilik.my" + link
    room_links.append(link)

    # Price
    price_tag = listing.select_one("div.room_price span") 
    raw_price = price_tag.get_text(strip=True) if price_tag else ""
    clean_price = (
        raw_price.replace(",", "")
        .replace("RM", "")
        .strip()
        .split()[0]
    )
    if clean_price.isdigit():
        clean_price = f"RM {float(clean_price):,.2f}"
    else:
        clean_price = f"RM {clean_price}"
    room_prices.append(clean_price)

    # Address
    address_tag = listing.select_one("i.fas.fa-map-marker-alt")
    raw_address = address_tag.find_next_sibling(string=True).strip() if address_tag else ""
    clean_address = raw_address.replace("|", " ").replace("\n", " ").strip()
    room_addresses.append(clean_address)

# Optional: preview
for i in range(len(room_links)):
    print(f"{i+1}. {room_addresses[i]} | {room_prices[i]} | {room_links[i]}")

# -------------------------------
# PART 2: Automated Data Entry (Selenium)
# -------------------------------

# Google Form link 
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScIx-azV9zFWkKyGm_EHE9iGyTRpNebojqzUdjrMkQR4pzx6w/viewform?usp=dialog"

# Configure Selenium WebDriver (Chrome)
driver = webdriver.Chrome()

for i in range(len(room_links)):
    driver.get(FORM_URL)
    time.sleep(2)  # wait for form to load

    # TODO: Update XPath/CSS selectors for your form fields
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_field.send_keys(room_addresses[i])
    price_field.send_keys(room_prices[i])
    link_field.send_keys(room_links[i])

    # Submit
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(1.5)  # brief pause before next entry

driver.quit()
