'''FINAL UI WITH SEARCH FILTERS'''
from dash import Dash, State, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import matplotlib
matplotlib.use('agg')                       #compatibility with webapps
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from BBSearch import LstSearch

searchFunc = LstSearch()
listings = []
data= {}
                                                
for listing in searchFunc.getResults():                 # Convert list objects to dicts
    listings.append({
        "name": getattr(listing, 'name', str(listing)),     # getattr converts to string if None
        "address": getattr(listing, 'address', ""),
        "numRooms": getattr(listing, 'numRooms', ""),
        "utilsIncluded": "yes" if getattr(listing, 'utilsIncluded', False) else "no",       #default to no if None
        "rentAmt": getattr(listing, 'rentAmt', ""),
        "notes": getattr(listing, 'notes', ""),
        "hostSite": getattr(listing, 'hostSite', ""),
        "listingURL": getattr(listing, 'listingURL', "")
    })

print(listings)

def aggregate_data(option):
    data = {}
    if option == 'Average Rent':
        for i in listings:             #clear list data
            host_site = i['hostSite']                  #xaxis values
            rent_amount = i['rentAmt']
            if host_site not in data:               
                data[host_site] = []                
            data[host_site].append(rent_amount)
        for site, amounts in data.items():
            data[site] = sum(amounts) / len(amounts)
        return data
    elif option == 'Average Number of Rooms':
        for i in listings:             #clear list data
            host_site = i['hostSite']
            num_rooms = i['numRooms']
            if host_site not in data:             #new key-value for site and info
                data[host_site] = []                #empty value to increment
            data[host_site].append(num_rooms)
        for site, rooms in data.items():
            data[site] = sum(rooms) / len(rooms)
        return data
    else:
        return {}
    
    
sites = [listing['hostSite'] for listing in listings]
room_avgs = [listing['rentAmt'] for listing in listings]
fig, ax = plt.subplots(figsize=(10, 5))     
ax.bar(sites, room_avgs, color='skyblue')                   #bar graph
ax.set_xlabel("Sites")
ax.set_ylabel("average rent")
plt.xticks(rotation=45)
plt.tight_layout()                                          #fits graph in window
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)
image_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")          #convert matplotlib graph to img


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

columns = [{"name": k, "id": k}
            for k in listings[0].keys()] if listings else []            # new list from dict keys

app.layout = html.Div([
    html.H1("ByteBungalow Listings"),
    dcc.Input(
        id='search-input',
        type='text',
        placeholder='Search by name or address...',
        debounce=True,                                                  # updates when hit enter
        style={'width': '300px'}
    ),
    dash_table.DataTable(
        id='results-table',
        columns=columns,
        data=listings,
        page_size=30, 
        style_table={'overflowX': 'auto', 'overflowY': 'auto'},          #table formatting
        style_cell={'textAlign': 'left', 'padding': '5px'},          
        style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'},
    ),
    html.H2("Average Number oflistings by Host Site"),
    dbc.Row([
        dbc.Col([                                               #dropdown for aggregation types
            dcc.Dropdown(
                id='category',
                value='Average Rent',
                clearable=False,
                options=[
                    {'label': 'Average Rent', 'value': 'Average Rent'},
                    {'label': 'Average Number of Rooms', 'value': 'Average Number of Rooms'}
                ])], width=4),
        dbc.Col([
            dcc.RangeSlider(
                id='graph-range',
                min=0,
                max=2000,
                value=[0, 10],
                marks={
                    0: {'label': '0'},
                    2000: {'label': '2000'}
                })], width=5)
    ]),
    dbc.Row([
            ]),
    dbc.Row([                                                   #display graph
        dbc.Col([
            html.Img(id="matplotlib-image", src=f"data:image/png;base64,{image_base64}", style={"width": "100%"})
        ], width=10)
    ], className="mt-3"),
])

@app.callback(
    Output('results-table', 'data'),
    Input('search-input', 'value')
)
def update_table(search_value):
    if not search_value or search_value.strip() == "":          #no search value
        return listings
    
    filtered_listings = []
    search_value = search_value.lower()
    
    for listing in listings:                                        #search for match in name or addr
        name = str(listing.get('name', '')).lower()                 
        address = str(listing.get('address', '')).lower()
        
        if search_value in name or search_value in address:
            filtered_listings.append(listing)
    return filtered_listings
    
@app.callback(
    Output("matplotlib-image", "src"),                  # input/output for graph
    [Input('results-table', 'data'),
     Input('category', 'value'),
     Input('graph-range', 'value')]                        #input table and dropdown    
)
def update_graph(table_data, category, graph_range):
    if category == 'Average Rent':
        data = aggregate_data(category)
        sites = list(data.keys())
        rent_avgs = list(data.values())
        fig, ax = plt.subplots(figsize=(10, 5))     
        ax.bar(sites, rent_avgs, color='skyblue')                   #bar graph
        ax.set_xlabel("Sites")
        ax.set_ylabel("average rent")
        ax.set_ylim(graph_range[0], graph_range[1])                #range
        plt.xticks(rotation=45)
        plt.tight_layout()                                          #fits graph in window
        buffer = BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")          #convert matplotlib graph to img
        return f"data:image/png;base64,{image_base64}"             
         
    elif category == 'Average Number of Rooms':
        data = aggregate_data(category)
        sites = list(data.keys())
        room_avgs = list(data.values())
        fig, ax = plt.subplots(figsize=(10, 5))     
        ax.bar(sites, room_avgs, color='skyblue')                   #bar graph
        ax.set_xlabel("Sites")
        ax.set_ylabel("average number of rooms")
        ax.set_ylim(graph_range[0], graph_range[1])
        plt.xticks(rotation=45)
        plt.tight_layout()                                          #fits graph in window
        buffer = BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode("ascii")          
        return f"data:image/png;base64,{image_base64}"                      #return graph
    else:
        return ""
    
if __name__ == '__main__':
    app.run(debug=False, port=8002)