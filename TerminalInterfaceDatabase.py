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
def main():
    #db = ListingDatabase()
    searchFunc = LstSearch()

    while True:
        os.system("cls")
        
        logo = (
"""     ____        _       ____                          _               
    |  _ \      | |     |  _ \                        | |              
    | |_) |_   _| |_ ___| |_) |_   _ _ __   __ _  __ _| | _____      __
    |  _ <| | | | __/ _ |  _ <| | | | '_ \ / _` |/ _` | |/ _ \ \ /\ / /
    | |_) | |_| | ||  __| |_) | |_| | | | | (_| | (_| | | (_) \ V  V / 
    |____/ \__, |\__\___|____/ \__,_|_| |_|\__, |\__,_|_|\___/ \_/\_/  
            __/ |                           __/ |                      
            |___/                           |___/                       """
        )
        
        print(f"{'─'*198}")
        print(logo)
        print(f"{'─'*198}")
        print("\tWelcome to the database interface!",
        "\nBelow is where your active search parameters are displayed. Please select from the provided menu to filter your results.\n",
        "\n\tWhat would you like to do?")
        print(f"{'─'*198}")

        print(f"\t Search Parameters:\n\t\tFavorited: {searchFunc.favorited} \n\t\tMin Rent: {searchFunc.minRent} \n\t\tMax Rent: {searchFunc.maxRent} \n\t\tRooms: {searchFunc.numRooms} \n\t\tUtilities: {searchFunc.utilsIncluded} \n\t\tHost Site: {searchFunc.hostSite}")

        print(f"{'─'*198}")

        print("""   Menu:
            1. Set Favorited
            2. Set Rent Range
            3. Set Rooms
            4. Set Utilities
            5. Set Host Site
            7. Get Results
            8. Sort Results (asc)
            9. Sort Results (desc)
            10. Clear Settings
            0. Exit
        """)
        

        while True:
            choice = input("Input: ")
            try:
                choice = int(choice)
                break
            except:
                print("Input must be a number")


        match choice:
            case 1: # Toggle favorited
                searchFunc.setIsFavorited(not searchFunc.favorited)
            case 2: # Set rent
                minRent = float(input("Min Rent: "))
                maxRent = float(input("Max Rent: "))
                searchFunc.setRent(minRent, maxRent)
            case 3: # Set rooms
                rooms = int(input("Rooms: "))
                searchFunc.setRooms(rooms)
            case 4: # Set utilities
                searchFunc.setUtilities(not searchFunc.utilsIncluded)
            case 5: # Set host site
                hostSite = input("Host Site: ")
                searchFunc.setHostSite(hostSite)
            case 7: # Get results
                searchFunc.getResults()
                print(f"\n\n\n{'─'*198}\n      Sorted Listings:\n")
                print(f"   ID    {'Listing Name':<50}  {'Rent':<11} Rooms Utils    Host Site       Address                          URL                              Notes  \n{'─'*198}")
                for listing in searchFunc.tempList:
                    print(listing)
                    print(f"{'─'*198}")
                input("Press ENTER to continue")
            case 8: # Sort (asc)
                searchFunc.criteria = None
                searchFunc.order = None
                while True:
                    try:
                        category = input("Category (1. for rent, 2. for rooms, 0. to exit): ")
                        category = int(category)
                        if category == 0:
                            break
                        elif category == 1:
                            category = "rent"
                        elif category == 2:
                            category = "rooms"
                        searchFunc.sortResults(category, "asc")
                        break
                    except:
                        print("Input must be 1, 2 or 0\n")
                        category = None
            case 9: # Sort (desc)
                searchFunc.criteria = None
                searchFunc.order = None
                while True:
                    try:
                        category = input("Category (1. for rent, 2. for rooms, 0. to exit): ")
                        category = int(category)
                        if category == 0:
                            break
                        elif category == 1:
                            searchFunc.sortResults("rent", "desc")
                        elif category == 2:
                            searchFunc.sortResults("rooms", "desc")
                        break
                    except:
                        print("Input must be 1, 2 or 0\n")
            case 10:    # Clear settings
                searchFunc.clearSettings()
            case 0: # Exit
                break
            case _: # Default
                print("Invalid Input")
                input("Press ENTER to continue")





    #db.close()

if __name__ == "__main__":
    main()