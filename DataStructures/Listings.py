import webbrowser as wb
import pyperclip

class Listing:
    """
    The Listing class, used to make objects for use in the database.

    Attributes:
        unitIndex (int): The index of the unit in the database
        name (str): The name of the listing
        address (str): The address of the listing
        numRooms (int): The number of rooms in the listing
        utilsIncluded (bool): Whether the utilities are included in the listing
        rentAmt (float): The rent amount of the listing
        listingURL (str): The URL of the listing
        hostSite (str): The site the listing is hosted on
        notes (str): Any notes about the listing
        favorited (bool): Whether or not the listing is favorited
    """
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
        """Returns a string representation of the Listing object in tabled format"""
        return f"{'✩' if self.favorited else ' ':<1} |{self.unitIndex:<3} | {self.name:<50} | ${self.rentAmt:<10} | {self.numRooms:<1} | {'✓' if self.utilsIncluded else ' ':<1} | {self.hostSite:<18} | {self.address:<30} | {self.listingURL:<30} | {self.notes:<25} |"
 
    def __repr__(self):
        """"""
        return f"Listing Object: {self.unitIndex} | {self.name} | {self.address} | {self.numRooms} | {self.utilsIncluded} | {self.rentAmt} | {self.listingURL} | {self.hostSite} | {self.notes} | {self.favorited}"
    
    # ____Listing Functions____
    def updateName(self, newName):
        """Updates the Name Attribute"""
        self.name = newName
    
    def updateAddress(self, newAddress):
        """Updates the Address Attribute"""
        self.address = newAddress
    
    def addNote(self, newNote):
        """Takes a str argument and updates the listing's notes attribute"""
        self.notes += "\n" + newNote

    def favorite(self):
        """Sets the listing as favorited"""
        self.favorited = True

    def unfavorite(self):
        """Unfavorites the listing
            * Might need to delete or change this later"""
        self.favorited = False

    def openListing(self):
        """Uses webbrowser to open the URL in the browser"""
        try:
            print(f"Opening {self.listingURL}")
            wb.open(self.listingURL)
        except Exception as e:
            print(f"There was arror opening the url for {self.name}'s listing: {self.listingURL}: {e}")

    def copyAddress(self):
        """Copies the address to the clipboard"""
        try:
            print(f"Copying {self.address} to clipboard")
            pyperclip.copy(self.address)
        except Exception as e:
            print(f"There was arror copying {self.name}'s address: {self.address} to the clipboard: {e}")