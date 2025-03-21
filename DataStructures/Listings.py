import webbrowser as wb
import pyperclip

class Listing:
    def __init__(self, unitIndex, name, address, numRooms, utilsIncluded, rentAmt, listingURL, hostSite, notes="", favorited=False):
        self.unitIndex = unitIndex
        self.name = name
        self.address = address
        self.numRooms = numRooms
        self.utilsIncluded = utilsIncluded
        self.rentAmt = rentAmt
        self.listingURL = listingURL
        self.hostSite = hostSite
        self.notes = notes
        self.favorited = favorited

    def __str__(self):
        return f"Listing Object: {self.unitIndex} | {self.name} | {self.address} | {self.numRooms} | {self.utilsIncluded} | {self.rentAmt} | {self.listingURL} | {self.hostSite} | {self.notes} | {self.favorited}"
    
    def __repr__(self):
        return f"Listing Object: {self.unitIndex} | {self.name} | {self.address} | {self.numRooms} | {self.utilsIncluded} | {self.rentAmt} | {self.listingURL} | {self.hostSite} | {self.notes} | {self.favorited}"
    
    # ____Listing Functions____
    def updateName(self, newName):
        self.name = newName
    
    def updateAddress(self, newAddress):
        self.address = newAddress
    
    def addNote(self, newNote):
        self.notes += "\n" + newNote

    def favorite(self):
        self.favorited = True

    def unfavorite(self):
        self.favorited = False

    # FINISH ME
    def openListing(self):
        print(f"Opening {self.listingURL}")
        wb.open(self.listingURL)

    # FINISH ME
    def copyAddress(self):
        print(f"Copying {self.address} to clipboard")
        pyperclip.copy(self.address)