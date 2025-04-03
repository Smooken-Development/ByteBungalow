from BBDatabase import ListingDatabase
from Listings import Listing as Lst
from BBSearch import LstSearch

db = ListingDatabase()
searchFunc = LstSearch()

"""listings = db.getAllListings()
print("____Listings:____")
print("Listing Object: unitIndex | name | address | numRooms | utilsIncluded | rentAmt | listingURL | hostSite | notes | favorited")
for listing in listings:
    print(listing)

db.close()"""

print("\n\n\n")

searchFunc.getResults()

searchFunc.sortResults("rent", "asc")
print("____Sorted Listings:____")
print("Listing Object: unitIndex | name | address | numRooms | utilsIncluded | rentAmt | listingURL | hostSite | notes | favorited")
for listing in searchFunc.temptList:
    print(listing)