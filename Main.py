# FIX ME: I can't get the stupid modules to import again
try:
    from DataStructures.Listings import Listing as Lst
except ImportError:
    print("Failed to import DataStructures.Listings")
    Lst = None
try:
    from DataStructures.Search import Search
except ImportError:
    print("Failed to import DataStructures.Search")
    Search = None
try:
    from DataStructures.Database import ListingDatabase
except ImportError:
    print("Failed to import ListingDatabase from DataStructures.Database")
    ListingDatabase = None


def main():
    if Lst is None:
        print("Failed to import DataStructures.Listings")
    if Search is None:
        print("Failed to import DataStructures.Search")
    if ListingDatabase is None:
        print("Failed to import ListingDatabase from DataStructures.Database")
    return

if __name__ == "__main__":
    main()