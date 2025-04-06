from BBDatabase import ListingDatabase
from DataStructures.Listings import Listing as Lst
from BBSearch import LstSearch
"""
    TO DO:
    1. Format "Listing" to accomadate CLI application
    2. Finish LstCacheImporter
        - Fix UpdateListing to update lisitng based off of unitIndex
        - Finish writeListingsToDB
    ✓3. Add documentation to BBDatabase
"""
"""def main():
    return
if __name__ == "__main__":
    main()"""


db = ListingDatabase()
searchFunc = LstSearch()

searchFunc.setRent(0, 1500)
searchFunc.setIsFavorited(True)
searchFunc.getResults()

#searchFunc.sortResults("rent", "asc")
print(f"\n\n\n{'─'*198}\n      Sorted Listings:\n")
print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
for listing in searchFunc.temptList:
    print(listing)
    print(f"{'─'*198}")

newListing = db.getListing(6)
newListing.favorite()
db.updateListing(newListing)

"""while True:
    print(
    Welcome to ByteBungalow!
    What would you like to do?
        
        1. Aggregate Listings (Update Database / Scour the Web for Listings!)
        2. 
)"""

db.close()




    