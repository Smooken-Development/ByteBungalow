from BBDatabase import ListingDatabase
from DataStructures.Listings import Listing as Lst
from BBSearch import LstSearch
import os
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

#newListing = db.getListing(6)
#newListing.favorite()
#db.updateListing(newListing)

while True:
    os.system("cls")
    print(f"{'─'*198}")
    print("\tWelcome to ByteBungalow!",
    "\n\tWhat would you like to do?")
    print(f"{'─'*198}")

    print(f"\t Search Parameters:\n\t\tFavorited: {searchFunc.favorited} \n\t\tMin Rent: {searchFunc.minRent} \n\t\tMax Rent: {searchFunc.maxRent} \n\t\tRooms: {searchFunc.numRooms} \n\t\tUtilities: {searchFunc.utilsIncluded} \n\t\tHost Site: {searchFunc.hostSite}")

    print("""
1. Set Favorited
2. Set Rent Range
4. Set Rooms
5. Set Utilities
6. Set Host Site
7. Get Results
8. Sort Results (asc)
9. Sort Results (desc)
10. Clear Settings
0. Exit
    """)
    choice = int(input("Input: "))

    match choice:
        case 1:
            searchFunc.setIsFavorited(not searchFunc.favorited)
        case 2:
            minRent = int(input("Min Rent: "))
            maxRent = int(input("Max Rent: "))
            searchFunc.setRent(minRent, maxRent)
        case 3:
            rooms = int(input("Rooms: "))
            searchFunc.setRooms(rooms)
        case 4:
            searchFunc.setUtilsIncluded(not searchFunc.utilsIncluded)
        case 5:
            hostSite = input("Host Site: ")
            searchFunc.setHostSite(hostSite)
        case 7:
            searchFunc.getResults()
            print(f"\n\n\n{'─'*198}\n      Sorted Listings:\n")
            print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
            for listing in searchFunc.temptList:
                print(listing)
                print(f"{'─'*198}")
            input("Presss any button to continue")
        case 8:
            searchFunc.sortResults("rent", "asc")
        case 9:
            searchFunc.sortResults("rent", "desc")
        case 10:
            searchFunc.clearSettings()
        case 0:
            break





db.close()




    