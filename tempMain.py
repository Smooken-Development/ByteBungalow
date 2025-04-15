from BBDatabase import ListingDatabase
from DataStructures.Listings import Listing as Lst
from BBSearch import LstSearch

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

import os

print(f"{'─'*198}")
print(firstOpening)
print(f"{'─'*198}")
userName = input("\tWhat would you like to be called?\n\t\tusername: ")
print("\n\n\tWelcome to ByteBungalow, " + userName + "!")
print(f"{'─'*198}")
print("\n\n\tPlease give me one moment while I load your program...")
os.system("cls")

print(f"{'─'*198}")
print(mainMenuText)
print(f"{'─'*198}")
choice = int(input("\n\nInput:  "))

while choice != 0:

    """match choice:
        case 1:
            os.system("cls")
            print("Aggregate Listings")
            input("Presss any button to continue")
        case 2:
            print("Editing your configurations")
        case 3:
            print("Viewing your listings")
        case 4:
            print("Formatting Database")
            # FINISH ME:
            print("Not Implemented Yet")
        case 0:
            print("Goodbye!")
            break"""
    
    
    
    
    os.system("cls")
    print(f"{'─'*198}")
    print(mainMenuText)
    print(f"{'─'*198}")
    choice = int(input("\n\nInput:  "))