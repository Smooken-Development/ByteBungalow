from Listings import Listing as Lst
from BBDatabase import ListingDatabase
import json

tempListings = []
tempPath = r"D:\1 - Computer Science Classes\ByteBungalow\ByteBungalow\DataStructures\tempListings.json"

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
        db.updateListing(listing)
    db.close()

# readFromListingCache(tempPath)

listing = Lst(
    unitIndex = 1,
    name = "Test",
    address = "Test",
    numRooms = 1,
    utilsIncluded = True,
    rentAmt = 1000,
    listingURL = "Test",
    hostSite = "Test",
    notes = "Test",
    favorited = True
)

#print(listing)
print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
#print(listing)
readFromListingCache(tempPath)
#writeListingsToDB()