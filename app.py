######### Import your libraries #######
import dash
from dash import dcc
from dash import html
import os

###### Set up variables
list_of_choices=[
			{
			"label": "Gorgeous Jupiter",
			"action": '1_hubble.jpeg'
		        },
		        {
			"label": "Giant Nebula",
			"action": "2_hubble.jpeg"
		        },
		        {
			"label": "Westerlund 2",
			"action": "3_hubble.jpeg"
		        },
		        {
			"label": "Eagle Nebula Pillars of Creation",
			"action": "4_hubble.jpeg"
		        },
		        {
			"label": "Molten Ring",
			"action": "5_hubble.jpeg"
		        },
		        {
			"label": "Webb's First Deep Field",
			"action": "JWST_first.jpeg"
		        }
		]
githublink = 'https://github.com/vkhvan/chuck_norris_execution'
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
## def display_value(whatever_you_chose):
def display_value(choice):
    label = list_of_choices[choice]["label"]
    action = list_of_choices[choice]["action"]
    return f'Enjoy this beautiful image of  {choice}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
