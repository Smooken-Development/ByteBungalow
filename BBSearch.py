from DataStructures.Listings import Listing as Lst
from BBDatabase import ListingDatabase
"""
    Module: BBSearch

    This module contains the Search class, which is used to store the parameters of a search.
    It provides methods to filter listings based on desired search criteria, such as number of rooms,
    rent, utilities included, host site, and favorited status.

    Classes:
        LstSearch: The search class, which encapsulates the search parameters and provides methods
                to retrieve and filter listings from the database.

    Functions:
        getResults: Retrieves and filters listings from the database based on search criteria.
        clearSettings: Clears the search parameters.
        setRooms: Sets the number of rooms to search for.
        setUtilities: Sets whether utilities are included in the rent.
        setRent: Sets the minimum and maximum rent to search for.
        setHostSite: Sets the host site to search for.
        setIsFavorited: Sets whether to search for favorited listings.
        sortResults: Sorts the search results based on the given criteria and order.
"""
class LstSearch:
    """
    The search class. Make an object with this class to filter listings based on your desired search criteria.

    # Example Usage:
        search = LstSearch()

        search.setRent(1000, 1500)

        print(search.getResults())

    # Operations:
    * getResults() # Use this function to activate the listing search
    * clearSettings() # Use this function to clear the search parameters
    * setRooms() # Searches for num of rooms (int)
    * setRent() # Searches for rent (int)
    * setIsFavorited() # Searches for favorited listings (bool)
    * setHostSite() # Set a specific host site to search for (str)
    * setUtilsIncluded() # Search for listings with utilities included (bool)
    * fillEmptyAttributes() # Safety function: see function for use case
    """
    def __init__(self, numRooms=None, utilsIncluded=None, minRent=None, maxRent=None, hostSite=None, favorited=None, criteria=None, order=None):
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
        self.criteria = criteria
        self.order = order

        self.tempList = []                              # This is to easily sort listings 

    def __str__(self)->str:
        return f"Search Parameters: {self.numRooms} {self.utilsIncluded} {self.minRent} {self.maxRent} {self.hostSite} {self.favorited}" 

    def __repr__(self)->str:
        """This is a default __repr__ method, it basically just shows the object's attributes if __str__ doesn't work"""
        return f"Search Parameters: {self.address} {self.numRooms} {self.utilsIncluded} {self.minRent} {self.maxRent} {self.hostSite} {self.favorited}"
    
    # _____Search Functions_____
    
    def clearSettings(self)->None:
        """Clears the Search Parameters"""
        # Set all parameters to None
        self.numRooms = None
        self.utilsIncluded = None
        self.minRent = None
        self.maxRent = None
        self.hostSite = None
        self.favorited = None

    def fillEmptyAttributes(self):
        """This corrects 'None' values for minRent and maxRent to 0 and positive infinity."""
        if self.minRent is None or self.minRent < 0:
            self.minRent = 0                                            # Set default minimum rent to 0
        if self.maxRent is None or self.maxRent < 0:
            self.maxRent = float('inf')                                    # No upper limit on rent

    def getResults(self):
        """
        Retrieves and filters listings from the database based on search criteria.
        """
        self.fillEmptyAttributes()
        allListings = self.db.getAllListings()

        self.tempList = [
            listing for listing in allListings
            if (self.numRooms is None or listing.numRooms == self.numRooms)
            and (self.utilsIncluded is None or listing.utilsIncluded == self.utilsIncluded)
            and (listing.rentAmt >= self.minRent)
            and (listing.rentAmt <= self.maxRent)
            and (self.hostSite is None or (listing.hostSite and listing.hostSite.lower() == self.hostSite.lower()))
            and (self.favorited is None or listing.favorited == self.favorited)
        ]

        self.sortResults(self.criteria, self.order)

        # print("Results:", self.tempList)
        return self.tempList

    def sortResults(self, criteria: str = None, order: str = None) -> None:
        """Sorts the Listing (Lst) based on the given criteria and order.
        
        Usage:

            criteria (str): The criteria to sort by (rent or rooms)
            order (str): The order to sort in ascending or descending (asc or desc)
        """
        try:
            # Matches criteria to listed criteria
            if criteria == "rent":
                self.criteria = "rent"
                # if rent: sorts rent by asc or desc
                if order == "asc":
                    self.order = "asc"
                    self.tempList = sorted(self.tempList, key=lambda x: x.rentAmt)
                else:
                    self.order = "desc"
                    self.tempList = sorted(self.tempList, key=lambda x: x.rentAmt, reverse=True)
            elif criteria == "rooms":
                self.criteria = "rooms"
                # if rooms: sorts rooms by asc or desc
                if order == "asc":
                    self.order = "asc"
                    self.tempList = sorted(self.tempList, key=lambda x: x.numRooms)
                else:
                    self.order = "desc"
                    self.tempList = sorted(self.tempList, key=lambda x: x.numRooms, reverse=True)
        except Exception as e:
            print(f"There was an error sorting results for {self.criteria} in {self.order} order: {e}")

    # _____Setters_____
    # These are to make life simpler when we're doing the UI. When using these
    # functions, make sure to call getResults() after.
    # When we put these in the UI interface, use these functions and map them
    # to the necessary buttons.
    def setRooms(self, numRooms):
        """Sets the number of rooms to search for."""
        # FUTURE IMPLEMENTATION:
        # Add numRooms to a range with minRooms and maxRooms
        self.numRooms = numRooms

    def setUtilities(self, utilsIncluded):
        """Sets whether to filter for only listings with utilities included."""
        self.utilsIncluded = utilsIncluded

    def setRent(self, minRent, maxRent):
        """Sets the rent range to search for.
        
        Set minRent for lower bound
        
        Set maxRent for upper bound
        """
        self.minRent = minRent
        self.maxRent = maxRent

    def setHostSite(self, hostSite):
        """Enter the exact host site you want to search for.
        
        # Example Usage:
            setHostSite("https://www.rent.com")
        # Valid Options:
            "https://www.rent.com"
            "https://www.trulia.com"
            "https://www.zillow.com"
        """
        self.hostSite = hostSite

    def setIsFavorited(self, favorited):
        """Sets whether to search for favorited listings"""
        self.favorited = favorited  # This doesn't favorite the listing, it's to search only for favorited listings in the DB
