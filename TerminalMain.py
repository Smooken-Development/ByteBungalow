from BBDatabase import ListingDatabase
from DataStructures.Listings import Listing as Lst
from BBSearch import LstSearch
import os
import LstCacheImporter
import webbrowser


def main():
    
    menu = (
"""
    Welcome to your one-stop shop for quickly finding metrics and listings across multiple platforms!

        What would you like to do?

        - (Aggregate) Aggregate Listings
        - (Listings) View the Listings Database
        - (Configs) Edit Configs
        - (Delete) Format the Database
        - (UI) Run the User Interface (Experimental)
        - (Exit) Exit

"""
    )

    logo = (
        """  ____        _       ____                          _               
 |  _ \      | |     |  _ \                        | |              
 | |_) |_   _| |_ ___| |_) |_   _ _ __   __ _  __ _| | _____      __
 |  _ <| | | | __/ _ |  _ <| | | | '_ \ / _` |/ _` | |/ _ \ \ /\ / /
 | |_) | |_| | ||  __| |_) | |_| | | | | (_| | (_| | | (_) \ V  V / 
 |____/ \__, |\__\___|____/ \__,_|_| |_|\__, |\__,_|_|\___/ \_/\_/  
         __/ |                           __/ |                      
        |___/                           |___/                       """
    )
    
    db = ListingDatabase()

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"{'─'*80}")
        print(logo)
        print(f"{'─'*80}")
        print(menu)

        # Convert to lower for ease-of-use
        try:
            choice = str(input("\tInput: ")).lower()
        except TypeError:
            print("Invalid Input")
            continue
        except EOFError:
            print("Exiting")
            break


        # Handling for invalid Inputs
        
        if choice in ["aggeregate", "agreagate", "agregate", "agregate", "aggeregate", "agregate listings", "aggreagate listings", "agregate listings", "aggeregate listings"]:
            choice = "aggregate"
        elif choice in ["listngs", "listiings", "listngs", "listiings", "listngs", "listiings"]:
            choice = "listings"
        elif choice in ["config", "configs", "config", "configs", "config", "configs", "config", "configs"]:
            choice = "configs"
        elif choice in ["delete", "del", "dlete", "del", "delete", "del", "dlete", "del", "delete", "del", "dlete", "del"]:
            choice = "delete"
        elif choice in ["exi", "exit", "exi", "exit", "exi", "exit", "exi", "exit", "exi", "exit", "exi", "exit", "exi", "exit"]:
            choice = "exit"
        elif choice == "oh yeah":
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Fantastic Sauce


        # Menu Options
        if choice == "aggregate" or choice == "1":
            # Aggregates listings and runs the webscrapers
            os.system("clear" if os.name == "posix" else "cls")
            os.system("python3 LstCacheImporter.py")
        elif choice == "listings" or choice == "2":
            # Opens the listings database interface
            os.system("clear" if os.name == "posix" else "cls")
            os.system("python3 TerminalInterfaceDatabase.py")
        elif choice == "configs" or choice == "3":
            # Opens the config interface
            os.system("clear" if os.name == "posix" else "cls")
            os.system("python3 Scripts/Setup.py")  # FINISHME:
        elif choice == "delete" or choice == "4":
            # Clears the database upon confirmation
            os.system("clear" if os.name == "posix" else "cls")
            print("WARNING: This will format the database and erase all listings.")
            confirmation = str(input("Are you sure? (type 'CONFIRM' to confirm or exit/0 to cancel): ")).lower()
            if confirmation == "confirm":
                print("Clearing Database...")
                db.clearDatabase()
                print("Database cleared!")
                input("Press ENTER to continue...")
            elif confirmation == "exit" or confirmation == "0":
                print("Cancelling operation...")
                pass
            
            else:
                print("Invalid Input")
                input("Press ENTER to continue...")
                pass
        elif choice == "ui" or choice == "5":
                try:
                    webbrowser.open("http://127.0.0.1:8002/")
                    os.system("python3 UX_Final2.py")
                except:
                    print("UI Final Failed opening! Skipping...")
                input("Press ENTER to continue...")
        elif choice == "exit" or choice == "0":
            return print("\n\n\tGoodbye!")
        else:
            print("Invalid Input")
            input("Press ENTER to continue...")


if __name__ == "__main__":
    main()