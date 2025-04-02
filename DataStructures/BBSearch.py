from Listings import Listing as Lst
from BBDatabase import ListingDatabase
"""
This module contains the Search class, which is used to store the parameters of a search.
"""
class LstSearch:
    """
    The search class

    Example Usage:
        search = LstSearch()

        search.setRent(1000, 1500)

        print(search.getResults())
    """
    def __init__(self, numRooms=None, utilsIncluded=None, minRent=None, maxRent=None, hostSite=None, favorited=None):
        """
        Initialize a Search object with the given parameters.

        Parameters:
        numRooms (int): Number of rooms in the listing
        utilsIncluded (bool): Whether utilities are included in the rent
        minRent (int): Minimum rent
        maxRent (int): Maximum rent
        hostSite (str): The website the listing is hosted on
        favorited (bool): Whether the listing is favorited or not
        """
        self.db = ListingDatabase()
        self.numRooms = numRooms
        self.utilsIncluded = utilsIncluded
        self.minRent = minRent
        self.maxRent = maxRent
        self.hostSite = hostSite
        self.favorited = favorited

        self.temptList = []    # This is to easily sort listings into

    def __str__(self):
        return f"Search Parameters: {self.numRooms} {self.utilsIncluded} {self.minRent} {self.maxRent} {self.hostSite} {self.favorited}" 

    def __repr__(self):
        return f"Search Parameters: {self.address} {self.numRooms} {self.utilsIncluded} {self.minRent} {self.maxRent} {self.hostSite} {self.favorited}"
    
    # _____Search Functions_____

    def clearSettings(self):
        # FINISHME:
        # Clear all attributes
        pass

    def fillEmptyAttributes(self):
        """
        Ensures that search parameters have default values to prevent query errors.
        """
        if self.minRent is None:
            self.minRent = 0  # Set default minimum rent to 0
        if self.maxRent is None:
            self.maxRent = float('inf')  # No upper limit on rent



    def getResults(self):
        """
        Retrieves and filters listings from the database based on search criteria.
        """
        # FINISHME:
        # fillEmptyAttributes()
        # Query the database
        # if input matches,
        #   populateTemptList(results)
        # else
        #   continue
        # sortResults(results)
        self.fillEmptyAttributes()
        allListings = self.db.getAllListings()

        self.temptList = [
            listing for listing in allListings
            if (self.numRooms is None or listing.numRooms == self.numRooms)
            and (self.utilsIncluded is None or listing.utilsIncluded == self.utilsIncluded)
            and (listing.rentAmt >= self.minRent)
            and (listing.rentAmt <= self.maxRent)
            and (self.hostSite is None or (listing.hostSite and listing.hostSite.lower() == self.hostSite.lower()))
            and (self.favorited is None or listing.favorited == self.favorited)
        ]

        print("Results:", self.temptList)
        return self.temptList

    def populateTempList(self):
        # FINISHME:
        # self.temptList = results
        # might need to use a loop of somekind here
        pass

    def populateTemptListALL(self):
        # FINISHME:
        # for item in database:
        #     self.temptList.append(item)
        pass

    def sortResults(self):
        # FINISHME:
        
        pass



    # _____Setters_____
    # These are to make life simpler when we're doing the UI
    def setRooms(self, numRooms):
        self.numRooms = numRooms

    def setUtilities(self, utilsIncluded):
        self.utilsIncluded = utilsIncluded

    def setRent(self, minRent, maxRent):
        self.minRent = minRent
        self.maxRent = maxRent

    def setHostSite(self, hostSite):
        self.hostSite = hostSite

    def setIsFavorited(self, favorited):
        self.favorited = favorited  # This doesn't favorite the listing, it's to search only for favorited listings in the DB


# FINISH ME: Finish putting test listings into the DB
search = LstSearch()
db = ListingDatabase()

newListing = Lst(20,
    "Beachfront Condo",
    "890 Birch Ave",
    2,
    False,
    2400,
    "http://example.com/listing20",
    "ApartmentList.com",
    "Ocean view",
    False
)

db.addListing(newListing)