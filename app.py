######### Import your libraries #######
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import os

###### Set up variables
list_of_choices=[
	{
		"label": "Gorgeous Jupiter",
		"action": "https://www.nasa.gov/sites/default/files/thumbnails/image/stsci-h-p2042a-f-1663x1663.png"
	},
	{
		"label": "Giant Nebula",
		"action": "http://www.rocketstem.org/wp-content/uploads/2015/04/001_pillars_of_creation_new.jpg"
	},
	{
		"label": "Westerlund 2",
		"action": "https://stsci-opo.org/STScI-01EVSTDDQX4KCV1CPTPPEEFNYB.png"
	},
	{
		"label": "Eagle Nebula Pillars of Creation",
		"action": "https://www.nasa.gov/sites/default/files/thumbnails/image/pillars_of_creation.jpg"
	},
	{
		"label": "Molten Ring",
		"action": "https://www.nasa.gov/sites/default/files/thumbnails/image/potw2050a.jpg"
	},
	{
		"label": "Webb's First Deep Field",
		"action": "https://s.hdnux.com/photos/01/26/47/23/22705401/3/1200x0.jpg"
	}
]
githublink = 'https://github.com/vkhvan/201-chuck_norris-callback'
heading1='Top 5 images from Hubble Telescope. And finally first image from an amazing JWST!'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Look at the sky!'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(src=image1, style={'width': 'auto', 'height': 'auto'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i["label"], 'value': choi} for choi,i in enumerate(list_of_choices)],
                value=0,
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Img(src='', style={'width': '50%', 'height':'50%'}, id='action'),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback([Output('your-output-here', 'children'), Output('action', 'src')],
              [Input('your-input-here', 'value')])
def display_value(choice):
    label = list_of_choices[choice]["label"]
    action = list_of_choices[choice]["action"]
    return f'Great choice going with a {label}.', action


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
