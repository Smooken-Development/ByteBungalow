from DataStructures.BBDatabase import ListingDatabase
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

db.updateListing(testListing)

listings = db.getAllListings()
for listing in listings:
    print(listing)

db.close()