from BBDatabase import ListingDatabase
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

searchFunc.setRent(0, 1200)
searchFunc.setRooms(2)
#searchFunc.setIsFavorited(False)
searchFunc.getResults()

#searchFunc.sortResults("rent", "asc")
#print(f"{'─'*198}\n      Sorted Listings:\n")
#print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
for listing in searchFunc.temptList:
    print(listing)
    print(f"{'─'*198}")

db.close()