######### Import your libraries #######
import dash
from dash import dcc
from dash import html
import os

###### Set up variables
list_of_choices=['Gorgeous Jupiter', 'Giant Nebula', 'Westerlund 2', 'Eagle Nebula Pillars of Creation', 'Molten Ring', "Webb's First Deep Field"]
list_of_pics=['1_hubble.jpeg', '2_hubble.jpeg', '3_hubble.jpeg', '4_hubble.jpeg', '5_hubble.jpeg', 'JWST_first.jpeg']
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
    html.Br(),
    dcc.Dropdown(id='your-input-here',
                options=[
				{'label': list_of_choices[0], 'action': list_of_pics[0]},
				{'label': list_of_choices[1], 'action': list_of_pics[1]},
				{'label': list_of_choices[2], 'action': list_of_pics[2]},
				{'label': list_of_choices[3], 'action': list_of_pics[3]},
				{'label': list_of_choices[4], 'action': list_of_pics[4]},
				{'label': list_of_choices[5], 'action': list_of_pics[5]}
			],
                value=list_of_pics[0],
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
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
