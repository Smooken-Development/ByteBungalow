'''import customtkinter as ctk
from tkinter import messagebox

class ByteBungalowUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ByteBungalow")

                                                         # main windowframes
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.top_frame = ctk.CTkFrame(self.main_frame)
        self.top_frame.pack(fill="x")
        self.middle_frame = ctk.CTkFrame(self.main_frame)
        self.middle_frame.pack(fill="both", expand=True)
        self.bottom_frame = ctk.CTkFrame(self.main_frame)
        self.bottom_frame.pack(fill="x")

                                                                            # top widgets
        self.search_label = ctk.CTkLabel(self.top_frame, text="Search by:")
        self.search_label.pack(side="left")

        self.search_entry = ctk.CTkEntry(self.top_frame)
        self.search_entry.pack(side="left")

        self.search_button = ctk.CTkButton(self.top_frame, text="Search")
        self.search_button.pack(side="left")

                                                                                    # middle widgets
        self.listings_label = ctk.CTkLabel(self.middle_frame, text="Rental Listings:")

        self.listings_label.pack(side="top")

        self.listings_tab = ctk.CTkTabview(self.middle_frame)
        self.listings_tab.pack(side="top", fill="both", expand=True)

                                                                                #  bottom  widgets
        self.stats_label = ctk.CTkLabel(self.bottom_frame, text="Statistics:")
        self.stats_label.pack(side="left")

        self.stats_button = ctk.CTkButton(self.bottom_frame, text="View Statistics")
        self.stats_button.pack(side="left")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = ctk.CTk()
    ui = ByteBungalowUI(root)
    ui.run()
'''
import sys
sys.path.append('C:/Users/cheap/ByteBungalow/ByteBungalow/DataStructures')
from DataStructures.Listings import Listing
from BBDatabase import ListingDatabase
from BBSearch import LstSearch
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import io
import base64

app = dash.Dash(__name__)                           # create app

db = ListingDatabase("listings.db")                 #database obj


graph_data = []
for listing in db.getAllListings():                #data to plot for graph
    graph_data.append(listing.unitIndex)
    graph_data.append(listing.name)
    graph_data.append(listing.rentAmt)
    graph_data.append(listing.numRooms)


plt.figure(figsize=(10, 6))
plt.bar(graph_data[0], graph_data[2])
plt.xlabel("Number of Rooms")
plt.ylabel("Rental Price")
plt.title("Listing Data")
plt.xticks(rotation=90)
plt.tight_layout()

img= io.BytesIO()                                 #save plot to image        
plt.savefig(img, format='png')
img.seek(0)

chart= base64.b64encode(img.getvalue()).decode()        #encode image

"data:image/png;base64,".format(chart) 

app.layout = html.Div([
    html.H1("Listing Database WebUI"),               # main title
    html.Div([
        html.Div([
            html.H2("Search Listings"),
            dcc.Input(id="search-input", type="text", placeholder="Search by name, address, or host site"),
            html.Button("Search", id="search-button", n_clicks=0)
        ]),
        html.H2("Listings"),                        #section 1 header
        html.Table([
            html.Thead([
                html.Tr([
                    html.Th("Unit Index"),
                    html.Th("Name"),
                    html.Th("Address"),
                    html.Th("Num Rooms"),
                    html.Th("Utils Included"),
                    html.Th("Rent Amt"),
                    html.Th("Listing URL"),
                    html.Th("Host Site"),
                    html.Th("Notes"),
                    html.Th("Favorited")
                ])
            ]),
            html.Tbody([
                html.Tr([                                   #populate table
                    html.Td(listing.unitIndex),
                    html.Td(listing.name),
                    html.Td(listing.address),
                    html.Td(listing.numRooms),
                    html.Td(listing.utilsIncluded),
                    html.Td(listing.rentAmt),
                    html.Td(listing.listingURL),
                    html.Td(listing.hostSite),
                    html.Td(listing.notes),
                    html.Td(listing.favorited)
                ]) for listing in db.getAllListings()               # get listings from db
            ])
        ]),


        html.Div([
            html.H2("Add Listing"),
            dcc.Input(id="unit-index", type="number", placeholder="Unit Index"),
            dcc.Input(id="name", type="text", placeholder="Name"),
            dcc.Input(id="address", type="text", placeholder="Address"),
            dcc.Input(id="num-rooms", type="number", placeholder="Num Rooms"),
            dcc.Input(id="utils-included", type="checkbox", placeholder="Utils Included"),
            dcc.Input(id="rent-amt", type="number", placeholder="Rent Amt"),
            dcc.Input(id="listing-url", type="text", placeholder="Listing URL"),
            dcc.Input(id="host-site", type="text", placeholder="Host Site"),
            dcc.Input(id="notes", type="text", placeholder="Notes"),
            dcc.Input(id="favorited", type="checkbox", placeholder="Favorited"),
            html.Button("Add Listing", id="add-listing-button", n_clicks=0)
        ]),


        html.Div([
            html.H2("Update Listing"),
            dcc.Input(id="update-unit-index", type="number", placeholder="Unit Index"),
            dcc.Input(id="update-name", type="text", placeholder="Name"),
            dcc.Input(id="update-address", type="text", placeholder="Address"),
            dcc.Input(id="update-num-rooms", type="number", placeholder="Num Rooms"),
            dcc.Input(id="update-utils-included", type="checkbox", placeholder="Utils Included"),
            dcc.Input(id="update-rent-amt", type="number", placeholder="Rent Amt"),
            dcc.Input(id="update-listing-url", type="text", placeholder="Listing URL"),
            dcc.Input(id="update-host-site", type="text", placeholder="Host Site"),
            dcc.Input(id="update-notes", type="text", placeholder="Notes"),
            dcc.Input(id="update-favorited", type="checkbox", placeholder="Favorited"),
            html.Button("Update Listing", id="update-listing-button", n_clicks=0)
        ]),


        html.Div([
            html.H2("Delete Listing"),
            dcc.Input(id="delete-unit-index", type="number", placeholder="Unit Index"),
            html.Button("Delete Listing", id="delete-listing-button", n_clicks=0)
        ]),


        html.Div([                                                  #display graph
            html.H2("Plot Listings"),
            dcc.Dropdown(id="plot-type", options=[
                {"label": "Bar Chart", "value": "bar"},
                {"label": "Scatter Plot", "value": "scatter"}
            ], value="bar"),
            html.Img(src="data:image/png;base64,{}".format(chart))
        ])
    ])
])

@app.callback(
    Output("listings-table", "children"),
    [Input("add-listing-button", "n_clicks")],
    [dash.dependencies.State("unit-index", "value"),
     dash.dependencies.State("name", "value"),
     dash.dependencies.State("address", "value"),
     dash.dependencies.State("num-rooms", "value"),
     dash.dependencies.State("utils-included", "value"),
     dash.dependencies.State("rent-amt", "value"),
     dash.dependencies.State("listing-url", "value"),
     dash.dependencies.State("host-site", "value"),
     dash.dependencies.State("notes", "value"),
     dash.dependencies.State("favorited", "value")],
)
def search_listings(n_clicks, search_value):
    if n_clicks > 0:
        search_ = LstSearch()
        search_.setRent(0,1500)          #default range
        search_results = search_.getResults()
        if search_results:
            return html.Div([html.P(f"Results for '{search_value}':"), 
            html.Ul([html.Li(f"{listing.name} - {listing.address}") for listing in search_results])])
        else:
            return html.P(f"No results found for '{search_value}'")
    return ""
def add_listing(n_clicks, unit_index, name, address, num_rooms, utils_included, rent_amt, listing_url, host_site, notes, favorited):
    if n_clicks > 0:
        listing = Listing(unit_index, name, address, num_rooms, utils_included, rent_amt, listing_url, host_site, notes, favorited)
        db.addListing(listing)
        return "Listing added successfully!"
    return ""

if __name__ == "__main__":
    app.run()
