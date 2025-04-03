from BBDatabase import ListingDatabase
from Listings import Listing as Lst

db = ListingDatabase()

testListing = Lst(
    unitIndex = 0,
    name = "Test Listing",
    address = "123 Test Street",
    numRooms = 3,
    utilsIncluded = True,
    rentAmt = 1000,
    listingURL = "https://testlisting.com",
    hostSite = "Test Site",
    notes = "Test Notes",
    favorited = True
)

"""db.updateListing(testListing)

listings = db.getAllListings()
for listing in listings:
    print(listing)

db.close()"""



import json
tempListings = []

with open(r"D:\1 - Computer Science Classes\ByteBungalow\ByteBungalow\DataStructures\tempListings.json", "r") as f:
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
        

