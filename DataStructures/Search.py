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
        # FINISHME:
        # Clear all attributes
        pass

    def fillEmptyAttributes(self):
        # FINISHME:
        # If any attributes have no input,
        # fill attributes with default values
        pass

    def getResults(self):
        # FINISHME:
        # fillEmptyAttributes()
        # Query the database
        # if input matches,
        #   populateTemptList(results)
        # else
        #   continue
        # sortResults(results)
        pass

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

    

    