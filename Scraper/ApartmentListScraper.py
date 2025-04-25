# import the required library
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re

def scrape():
# instantiate a Chrome options object
    print(f"Starting ApartmentList Scraper...")
    options = webdriver.ChromeOptions()

    # set the options to use Chrome in headless mode and ignore sandbox mode for anti-bot detection
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    
    # initialize an instance of the Chrome driver 
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.apartmentlist.com/apartments-near-me')

    driver.implicitly_wait(10)

    listing_cards = driver.find_elements(By.XPATH, '//div[@aria-label][contains(@aria-label, "Listing card")]')

    all_housing_data = []

    i = 0
    for i in range(len(listing_cards)):
        card = listing_cards[i]
        full_text = card.text

        # Extract number of beds using regex
        bed_match = re.search(r'(\d+)\s+bed', full_text, re.IGNORECASE)
        beds = bed_match.group(0) if bed_match else "N/A"
        # Parse the beds to integer
        try:
            beds = int(beds[0])
        except ValueError:
            print("There was an error parsing the number of beds to integer")
            beds = 0
        
        # Extract the rent amount
        rent_amount = driver.find_elements(By.XPATH, '//div[contains(@class, "text-subheading-medium") and contains(text(), "$")]')[i].text
        # Parse the rent amount to float
        try:
            rent_amount = re.sub(r'[^\d]', '', rent_amount)
            rent_amount = float(rent_amount)
        except ValueError:
            print("There was an error subtracting symbols from the rent amount and parsing to float.")
            rent_amount = 0

        try:
            housing_data_elements = {
                'unitIndex': 0,
                'name': driver.find_elements(By.XPATH, '//a[contains(@class, "group-loading:loading-darker") and contains(@class, "text-subheading-medium") and contains(@href, "/nm/")]')[i].text,
                'address': driver.find_elements(By.CSS_SELECTOR, 'div[aria-label^="Address for"] > span')[i].text,
                'numRooms': beds,
                'utilsIncluded': False,
                'rentAmt': rent_amount,
                'listingURL': driver.find_elements(By.XPATH,'//a[contains(@class, "group-loading:loading-darker") and contains(@class, "text-subheading-medium") and contains(@class, "no-underline") and contains(@class, "truncate")]')[i].get_attribute('href'),
                'hostSite': 'apartmentlist',
                'notes': '',
                'favorited': False
            }
            all_housing_data.append(housing_data_elements)
        except IndexError:
            print(f"Skipping card #{i+1} due to missing data")

    driver.quit()

    # save the data to a JSON file
    import os
    cache_file = 'TempCache.json'

    # error handling because it broke
    if os.path.exists(cache_file):
        try:
            # read the existing cache
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache = json.load(f)
                if not isinstance(cache, list):
                    print("Warning: Cache is not a list. Reinitializing...")
                    cache = []
        except json.JSONDecodeError:
            print("Warning: Cache is not a valid JSON file. Reinitializing...")
            cache = []
    else:
        print("No cache file found. Starting Fresh.")
        cache = []
    
    # add the new data to the cache
    all_housing_data = cache + all_housing_data

    # save the updated cache
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(all_housing_data, f, indent=4, ensure_ascii=False)

    print(f"Finished ApartmentList Scraper!")

#test

scrape()