# FIX ME: I can't get the stupid modules to import again
print("Running Main.py")
print("Importing DataStructures.Listings")
from DataStructures.Listings import Listing as Lst
print("Imported DataStructures.Listings")
print("Importing DataStructures.Database")
from DataStructures.Database import ListingDatabase
print("Imported DataStructures.Database")


def main():
    print("Running Main.py")
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

    db.addListing(testListing)
    print("Added test listing to database")

    listings = db.getAllListings()
    for listing in listings:
        print(listing)

    db.close()

print("Accessing Main.py")
main()