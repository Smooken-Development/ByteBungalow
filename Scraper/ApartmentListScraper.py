# import the required library
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re

def scrape():
# instantiate a Chrome options object
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
        try:
            housing_data_elements = {
                'name': driver.find_elements(By.XPATH, '//a[contains(@class, "group-loading:loading-darker") and contains(@class, "text-subheading-medium") and contains(@href, "/nm/")]')[i].text,
                'address': driver.find_elements(By.CSS_SELECTOR, 'div[aria-label^="Address for"] > span')[i].text,
                'numRooms': beds,
                'utilsIncluded': False,
                'rentAmt': driver.find_elements(By.XPATH, '//div[contains(@class, "text-subheading-medium") and contains(text(), "$")]')[i].text,
                'listingURL': driver.find_elements(By.XPATH,'//a[contains(@class, "group-loading:loading-darker") and contains(@class, "text-subheading-medium") and contains(@class, "no-underline") and contains(@class, "truncate")]')[i].get_attribute('href'),
                'hostSite': 'apartmentlist',
                'notes': '',
                'favorited': False
            }
            all_housing_data.append(housing_data_elements)
        except IndexError:
            print(f"Skipping card #{i+1} due to missing data")

    driver.quit()

    #Save all housing data to a json file
    with open('ApartmentList_Listings.json', 'w', encoding='utf-8') as f:
        json.dump(all_housing_data, f, indent=4, ensure_ascii=False)

#test


