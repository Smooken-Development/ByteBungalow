
from DataStructures.BBDatabase import ListingDatabase
from DataStructures.Listings import Listing as Lst
from DataStructures.BBSearch import LstSearch


def main():
    if Lst is None:
        print("Failed to import DataStructures.Listings")
    if LstSearch is None:
        print("Failed to import DataStructures.Search")
    if ListingDatabase is None:
        print("Failed to import ListingDatabase from DataStructures.Database")
    return

if __name__ == "__main__":
    main()