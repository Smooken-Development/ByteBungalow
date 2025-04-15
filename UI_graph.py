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

'''Read from list of listings'''

db = ListingDatabase("listings.db")                 #database obj


xaxis_data = []
for listing in db.getAllListings():                #pass from BBDatabase
    xaxis_data.append(listing.name)

yaxis_data = []
for listing in db.getAllListings():                #DD list attributes
    yaxis_data.append(listing.rentAmt)


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
    html.H1("ByteBungalow"),
    html.Div([
        html.Div([
            html.Label("Search Listings"),
            dcc.Input(id="search-input", type="text", placeholder="Search Listings..."),
            html.Button("Search", id="search-button"),
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            html.Label("Add Listing"),
            dcc.Input(id="unit-index", type="text", placeholder="Unit Index"),
            dcc.Input(id="name", type="text", placeholder="Name"),
            dcc.Input(id="address", type="text", placeholder="Address"),
            dcc.Input(id="num-rooms", type="number", placeholder="Number of Rooms"),
            dcc.Input(id="utils-included", type="text", placeholder="Utilities Included"),
            dcc.Input(id="rent-amt", type="number", placeholder="Rent Amount"),
            dcc.Input(id="listing-url", type="text

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
def search_listings(n_clicks, search_value):                            #search bar
    if n_clicks > 0:
        search_ = LstSearch()
        search_.setRent(0,1500)                         #default range
        search_results = search_.getResults()
        if search_results:
            return html.Div([html.P(f"Results for '{search_value}':"),   #display results
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
