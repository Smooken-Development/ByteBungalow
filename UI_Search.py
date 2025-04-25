from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import matplotlib
matplotlib.use('agg')                       #compatibility with webapps
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from BBSearch import LstSearch

searchFunc = LstSearch()
data = {}
'''nav bar/ search function '''
searchparams =                 #get listings from BBsearch
for i in searchparams:                       #get listings from BBsearch
    if 


'''Rent Averages by Host Site'''
for i in searchFunc.getResults():            #get listings from BBsearch    
    host_site = i.hostSite                  #xaxis values
    rent_amount = i.rentAmt
    if host_site not in data:               
        data[host_site] = []                
    data[host_site].append(rent_amount)
print(data)                                     #debug
rent_avgs = [sum(rent_amounts) / len(rent_amounts) for rent_amounts in data.values()]   #avg rent

'''Average Number of rooms'''
for i in data.values():             #clear list data
    i.clear()
for i in searchFunc.getResults():
    host_site = i.hostSite
    num_rooms = i.numRooms
    if host_site not in data:             #new key-value for site and info
        data[host_site] = []                #empty value to increment
    data[host_site].append(num_rooms)
print(data)
room_avgs = [sum(num_rooms) / len(num_rooms) for num_rooms in data.values()]   #avg num rooms



sites = list(data.keys())                           # dict keys

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


'''Display initial graph'''
fig, ax = plt.subplots(figsize=(10, 5))     
ax.bar(sites, room_avgs, color='skyblue')           #bar graph
ax.set_xlabel("Sites")
ax.set_ylabel("average rent")
plt.xticks(rotation=45)
plt.tight_layout()                          #fits graph in window


buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)
image_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")  #convert matplotlib graph to img     

app.layout = dbc.Container([
    html.H1("Byte Bungalow", style={"textAlign": "center"}),            #title
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
                ]) for listing in searchFunc.tempList               # get listings from db
            ])
        ]),
    
        html.Div([

        dcc.RangeSlider( 0,20, marks= None, value=[0, 20], id="range-slider"),         #slider for range
        html.Div(id="output-container-range-slider"),         
        ]),       
        

    dbc.Row([                                                   #display graph
        dbc.Col([
            html.Img(id="matplotlib-image", src=f"data:image/png;base64,{image_base64}", style={"width": "100%"})
        ], width=10)
    ], className="mt-3"),
])
@callback(
    Output("output-container-range-slider", "children"),
    Output("matplotlib-image", "src"),
    Input("range-slider", "value")
    Input("search-input", "value")
)

def update_graph(val_list):
    fig, ax = plt.subplots(figsize=(10, 5))     
    ax.bar(sites, room_avgs, color='skyblue')           #bar graph
    ax.set_xlabel("Sites")
    ax.set_ylabel("average rent")
    ax.set_ylim(val_list[0], val_list[1])                   #yaxis range
    plt.xticks(rotation=45)
    plt.tight_layout()                          #fits graph in window

    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")  #convert matplotlib graph to img    

    return "", f"data:image/png;base64,{image_base64}"      #return graph

if __name__ == "__main__":
    app.run(debug=False, port=8002) 