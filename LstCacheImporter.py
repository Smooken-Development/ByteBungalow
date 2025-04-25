from DataStructures.Listings import Listing as Lst
from BBDatabase import ListingDatabase
from BBSearch import LstSearch
import json
import os

tempListings = []
tempPath = "TempCache.json"

def runScrapers():
    """A short script to run the webscrapers."""
    # FINISHME:
    print("Running Scrapers...")
    os.system("python Scraper/WebScraper.py")
    print("Scrapers Finished!")

def readFromListingCache(path):
    """
    Reads listings from a JSON file and appends them to the tempListings list. Returns the list of listings.

    Args:
        path (str): The path to the JSON file containing the listings data.

    The function reads each listing from the specified JSON file, creates a Listing
    object for each, and appends it to the tempListings list. It then prints out
    each listing.

    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        json.JSONDecodeError: If the file at the specified path is not a valid JSON file.
    """

    try:
        with open(path, "r") as f:
            data = json.load(f)
            for listing in data:
                tempListings.append(Lst(
                    unitIndex = listing["unitIndex"],
                    name = listing["name"],
                    address = listing["address"],
                    numRooms = listing["numRooms"],
                    utilsIncluded = listing["utilsIncluded"],
                    rentAmt = listing["rentAmt"],
                    listingURL = listing["listingURL"],
                    hostSite = listing["hostSite"],
                    notes = listing["notes"],
                    favorited = listing["favorited"]
                ))

        print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
        for listing in tempListings:
            print(listing)
        
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    except json.JSONDecodeError:
        print(f"The file {path} is not a valid JSON file.")

def writeListingsToDB():
    """
    Compares listings in the temporary cache with those in the database and updates the database accordingly.

    The function retrieves all listings from the database and compares them with those in the tempListings list.
    If a listing from tempListings does not exist in the database (based on address comparison), it is added to the database.
    If a listing already exists, it is updated in the database.

    Note: The actual database operations (add/update) are currently commented out.

    The function assumes that the database connection will be closed after operations are performed.
    """

    db = ListingDatabase()
    comparisonList = db.getAllListings()

    # FIXME: This may need a better sort algorithm later down the line, depending on the size of the DB per user
    for listing in tempListings:
        match = False
        for compListing in comparisonList:
            if listing.address == compListing.address:
                match = True
                break

        if not match:
            db.addListing(listing)
            print(f"Adding Listing {listing.unitIndex} | {listing.name} to DB")
            print()
        elif match:
            print(f"Updating Listing {listing.unitIndex} | {listing.name} in DB")
            db.updateListing(listing)
            print()
    db.close()

def main():
    """
    Reads listings from a JSON file and writes them to a database.
    
    This is the main script to write to the database."""
    runScrapers()
    readFromListingCache(tempPath)
    writeListingsToDB()
    print(f"[FINISHED] All Listings has been imported from {tempPath}!")


if __name__ == "__main__":
    main()
    input("Press ENTER to continue...")