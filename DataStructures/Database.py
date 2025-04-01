from Listings import Listing
import Search
import sqlite3


class ListingDatabase:
    # def init
    def __init__(self, dbName="listings.db"):
        self.conn = sqlite3.connect(dbName) # con is short for connect
        self.cursor = self.conn.cursor()
        self.createTable()

    def createTable(self):
        '''
        Creates the ListingsTable in the database if it does not already exist.

        unitIndex: The index of the unit in the database
        name: The name of the listing
        address: The address of the listing
        numRooms: The number of rooms in the listing
        utilsIncluded: Whether the utilities are included in the listing
        rentAmt: The rent amount of the listing
        listingURL: The URL of the listing
        hostSite: The site the listing is hosted on
        notes: Any notes about the listing
        favorited: Whether or not the listing is favorited
        '''
        self.cursor.execute(''''
            CREATE TABLE IF NOT EXISTS ListingsTable (
                unitIndex INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                numRooms INTEGER,
                utilsIncluded BOOLEAN,
                rentAmt REAL,
                listingURL TEXT,
                hostSite TEXT,
                notes TEXT,
                favorited BOOLEAN
            )
        ''')
        self.conn.commit()

    def addListing(self, listing: Listing):
        if not isinstance(listing, Listing):
            raise TypeError(f"{listing} must be of type Listing")
        self.cursor.execute('''
            INSERT INTO ListingsTable (unitIndex, name, address, numRooms, utilsIncluded, rentAmt, listingURL, hostSite, notes, favorited)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (listing.unitIndex, listing.name, listing.address, listing.numRooms, listing.utilsIncluded, listing.rentAmt, listing.listingURL, listing.hostSite, listing.notes, listing.favorited))
        self.conn.commit()

    def getAllListings(self):
        self.cursor.execute('''
            SELECT * FROM ListingsTable
        ''')
        listings = self.cursor.fetchall()
        
    

    # funcitons
    pass


