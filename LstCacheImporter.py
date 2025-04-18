from DataStructures.Listings import Listing as Lst
from BBDatabase import ListingDatabase
import json

tempListings = []
tempPath = "TempCache.json"

def readFromListingCache(path):
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

    for listing in tempListings:
        print(listing)

def writeListingsToDB():
    db = ListingDatabase()
    for listing in tempListings:
        db.addListing(listing)
    db.close()

print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
readFromListingCache(tempPath)
# writeListingsToDB()

