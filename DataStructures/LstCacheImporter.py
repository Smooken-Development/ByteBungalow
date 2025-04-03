from Listings import Listing as Lst
import json
tempListings = []

with open(r"D:\1 - Computer Science Classes\ByteBungalow\ByteBungalow\DataStructures\tempListings.json", "r") as f:
    data = json.load(f)
    for listing in data:
        tempListings.append(Lst(
            unitIndex = listing["unitIndex"],
            name = listing["name"],
            address = listing["address"],
            numRooms = listing["numRooms"],
            utilsIncluded = listing["utilsIncluded"],
            rentAmt = listing["rentAmt"],
            listingURL = listing["listingURL"],
            hostSite = listing["hostSite"],
            notes = listing["notes"],
            favorited = listing["favorited"]
        ))

for listing in tempListings:
    print(listing)