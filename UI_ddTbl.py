import sys
sys.path.append('C:/Users/cheap/ByteBungalow/ByteBungalow/')
from DataStructures.Listings import Listing
from BBDatabase import ListingDatabase
from BBSearch import LstSearch

import dash
from dash import dcc
from dash import html
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
 
#import plotly.graph_objs as go

import matplotlib.pyplot as plt
import io
import base64

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])                           # create app

db = ListingDatabase("listings.db")                 #database obj


graph_data = []
for listing in db.getAllListings():                #pass from BBDatabase
    graph_data.append(listing.unitIndex)
    graph_data.append(listing.name)
    graph_data.append(listing.rentAmt)          #data to plot for graph
    graph_data.append(listing.numRooms)


plt.figure(figsize=(10, 6))
plt.bar(graph_data[2], graph_data[3])
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
        search_.setRent(0,1500)                         #default range
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