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

firstOpening = (
"""
            Hello! Welcome to ByteBungalow!
            
    Your one-stop shop for analyzing rental property data from some of the major rental sites and providing insightful graphs and filterable listings.
"""
)
userName = ""
searchCity = ""
mainMenuText = (
"""
Welcome to ByteBungalow!
    What would you like to do?
        
        1. Aggregate Listings (Update Database / Scour the Web for Listings!)
        2. Edit your configurations
        3. View your listings
        4. Format Database
        0. Exit

"""
)

db = ListingDatabase()
searchFunc = LstSearch()

searchFunc.setRent(0, 1500)
searchFunc.setIsFavorited(True)
searchFunc.getResults()

searchFunc.sortResults("rent", "desc")
print(f"\n\n\n{'─'*198}\n      Sorted Listings:\n")
print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
for listing in searchFunc.temptList:
    print(listing)
    print(f"{'─'*198}")

#newListing = db.getListing(6)
#newListing.favorite()
#db.updateListing(newListing)

"""import os

print(f"{'─'*198}")
print(firstOpening)
print(f"{'─'*198}")
#userName = input("\tWhat would you like to be called?\n\t\tusername: ")
print("\n\n\tWelcome to ByteBungalow, " + userName + "!")
print(f"{'─'*198}")
print("\n\n\tPlease give me one moment while I load your program...")
os.system("cls")



while choice != 0:
    os.system("cls")
    print(f"{'─'*198}")
    print(mainMenuText)
    print(f"{'─'*198}")
    choice = int(input("\n\nInput:  "))

    match choice:
        case 1:
            print("Aggregate Listings")
        case 2:
            print("Editing your configurations")
        case 3:
            print("Viewing your listings")
        case 4:
            print("Formatting Database")
        case 0:
            print("Goodbye!")
            break"""


db.close()




    