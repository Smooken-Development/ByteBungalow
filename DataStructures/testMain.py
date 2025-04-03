from BBDatabase import ListingDatabase
from Listings import Listing as Lst
from BBSearch import LstSearch

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
print("____Listings:____")
print("Listing Object: unitIndex | name | address | numRooms | utilsIncluded | rentAmt | listingURL | hostSite | notes | favorited")
for listing in listings:
    print(listing)

db.close()