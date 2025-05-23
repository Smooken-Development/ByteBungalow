from DataStructures.Listings import Listing
import sqlite3

class ListingDatabase:
    """
    A class representing a database of listings. Allows you to interact directly with the current database.
    """
    # def init
    def __init__(self, dbName="listings.db"):
        self.conn = sqlite3.connect(dbName) # conn is short for connect
        self.cursor = self.conn.cursor()
        self.createTable()

    def createTable(self):
        '''
        Creates the ListingsTable in the database if it does not already exist.

        * unitIndex: The index of the unit in the database
        * name: The name of the listing
        * address: The address of the listing
        * numRooms: The number of rooms in the listing
        * utilsIncluded: Whether the utilities are included in the listing
        * rentAmt: The rent amount of the listing
        * listingURL: The URL of the listing
        * hostSite: The site the listing is hosted on
        * notes: Any notes about the listing
        * favorited: Whether or not the listing is favorited
        '''
        self.cursor.execute('''
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
        """
        Adds a listing to the database. The listing must be of type Listing.

        Args:
            listing (Listing): The listing to add to the database

        Raises:
            TypeError: If the listing is not of type Listing
            sqlite3.Error: If there is a database error
        """
        # If listing already exists, add 1 to unitIndex and addListing
        if not isinstance(listing, Listing):
            raise TypeError(f"{listing} must be of type Listing")
        try:
            self.cursor.execute('''
                SELECT * FROM ListingsTable WHERE unitIndex = ?
            ''', (listing.unitIndex,))
            if self.cursor.fetchone() is not None:
                print(f"{listing.name} already exists in the database. Adding 1 to the unitIndex and adding the listing.")
                listing.unitIndex += 1
                self.addListing(listing)
            else:
                self.cursor.execute('''
                    INSERT INTO ListingsTable (unitIndex, name, address, numRooms, utilsIncluded, rentAmt, listingURL, hostSite, notes, favorited)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (listing.unitIndex, listing.name, listing.address, listing.numRooms, listing.utilsIncluded, listing.rentAmt, listing.listingURL, listing.hostSite, listing.notes, listing.favorited))
                self.conn.commit()
                print(f"Added {listing.name} to the database")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def getAllListings(self):
        """
        Retrieves all listings from the database.

        Returns:
            List[Listing]: A list of all listings in the database
        """

        self.cursor.execute('''
            SELECT * FROM ListingsTable
        ''')
        listings = self.cursor.fetchall()
        return [Listing(*listing) for listing in listings]
    
    def getListing(self, unitIndex):
        self.cursor.execute('''
            SELECT * FROM ListingsTable WHERE unitIndex = ?
        ''', (unitIndex,))
        listing = self.cursor.fetchone()
        return Listing(*listing) if listing else None
    
    def deleteListing(self, unitIndex):
        """
        Deletes a listing from the database based on unitIndex.
        """
        self.cursor.execute('''
            DELETE FROM ListingsTable WHERE unitIndex = ?
        ''', (unitIndex,))
        self.conn.commit()

    def updateListing(self, listing: Listing):
        """
        Updates an existing listing in the database with new values.

        # Example Usage:
        To update individual attributes for a listing:

            listing = db.getListing(unitIndex)
            listing.favorite(True)
            db.updateListing(listing)

        You will need to look at the functions within the listing class to see which functions update the attributes.

        Args:
            listing (Listing): The listing object containing updated information. 
                            The listing must have a valid unitIndex that exists 
                            in the database to be updated.

        Raises:
            TypeError: If the listing is not of type Listing.
        """
        self.cursor.execute('''
            UPDATE ListingsTable
            SET name = ?, address = ?, numRooms = ?, utilsIncluded = ?, rentAmt = ?, listingURL = ?, hostSite = ?, notes = ?, favorited = ?
            WHERE unitIndex = ?
        ''', (listing.name, listing.address, listing.numRooms, listing.utilsIncluded, listing.rentAmt, listing.listingURL, listing.hostSite, listing.notes, listing.favorited, listing.unitIndex))
        self.conn.commit()
        print(f"Updated {listing.name} in the database")

    def close(self):
        """
        Closes the connection to the database.
        
        This method should be called to ensure that the database connection 
        is properly closed when it is no longer needed.
        """
        self.conn.close()

    def sizeOfDatabase(self):
        """Get the number of entries in the database"""
        self.cursor.execute('''
            SELECT COUNT(*) FROM ListingsTable
        ''')
        return self.cursor.fetchone()[0]

    def clearDatabase(self):
        """This will be to factor the database. Deleting all entries."""
        self.cursor.execute('''
            DELETE FROM ListingsTable
        ''')
        self.conn.commit()
        print(f"Database {self.conn} cleared")
        return