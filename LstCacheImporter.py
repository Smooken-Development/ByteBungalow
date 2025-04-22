from DataStructures.Listings import Listing as Lst
from BBDatabase import ListingDatabase
import json

tempListings = []
tempPath = "TempCache.json"

def readFromListingCache(path):
    """
    Reads listings from a JSON file and appends them to the tempListings list.

    Args:
        path (str): The path to the JSON file containing the listings data.

    The function reads each listing from the specified JSON file, creates a Listing
    object for each, and appends it to the tempListings list. It then prints out
    each listing.
    """

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
    """
    Writes all listings in the tempListings list to the database.

    The function takes no arguments and returns no values. It creates a ListingDatabase
    object, adds each listing in the tempListings list to the database using the
    addListing method, and then closes the database.
    """
    
    db = ListingDatabase()
    for listing in tempListings:
        db.addListing(listing)
    db.close()

# tempPath = r"D:\1 - Computer Science Classes\ByteBungalow\ByteBungalow\DataStructures\tempListings.json"  # DELETE ME:
#print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
#readFromListingCache(tempPath)
# writeListingsToDB()

