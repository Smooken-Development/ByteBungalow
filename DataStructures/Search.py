from Listings import Listing as Lst
class Search:
    def __init__(self, numRooms, utilsIncluded, minRent, maxRent, hostSite, favorited):
        self.numRooms = numRooms
        self.utilsIncluded = utilsIncluded
        self.minRent = minRent
        self.maxRent = maxRent
        self.hostSite = hostSite
        self.favorited = favorited

        self.temptList = Lst([])    # This is to easily sort listings into

    def __str__(self):
        return f"Search Parameters: {self.numRooms} {self.utilsIncluded} {self.minRent} {self.maxRent} {self.hostSite} {self.favorited}" 

    def __repr__(self):
        return f"Search Parameters: {self.address} {self.numRooms} {self.utilsIncluded} {self.minRent} {self.maxRent} {self.hostSite} {self.favorited}"
    
    # _____Search Functions_____

    def clearSettings(self):
        pass

    def fillEmptyAttributes(self):
        pass

    def getResults(self):
        pass

    def populateTempList(self):
        pass

    def populateTemptListALL(self):
        pass

    def sortResults(self):
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

    

    