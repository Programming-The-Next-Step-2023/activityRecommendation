# App for Programming - The Next Step
# Fleur Korzilius
# May 2023

import pandas as pd
import numpy as np
from dash import Dash, callback, Output, Input, dcc, html, dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "What should I do?"
# import data from this dataframe for activity input for now
df = pd.read_csv(r'C:\Research Master Psychology UVA\Semester IV\Programming - The Next Step\activities.csv', encoding="ISO-8859-1", sep=";")
font = 'calibri'

app.layout = html.Div([
    html.H1(children='What should I do today?',
            style={'textAlign': 'center', 'color': 'black', 'fontSize': 30, 'font-family': font}),
    dcc.Tabs([
        dcc.Tab(label = "How do I feel?",
                style={'color': 'black', 'fontSize': 20, 'font-family': font},
                children=[
            html.Div([
                html.H2(children='Physical energy is ... (1 = very low, 5 = energized)',
                        style={'textAlign': 'left', 'color': 'black', 'fontSize': 20, 'font-family': font}),
                dcc.Slider(1, 5, 1, value=1, id='physical'),

                html.H2(children='Mental energy is ...(1 = very low, 5 = energized)',
                style={'textAlign': 'left', 'color': 'black', 'fontSize': 20, 'font-family': font}),
                dcc.Slider(1, 5, 1, value=1, id='mental'),

                html.H2(children='Do you want to leave the house?',
                style={'textAlign': 'left', 'color': 'black', 'fontSize': 20, 'font-family': font}),
                dcc.RadioItems(options=['Yes', 'No'], value='Yes', id='leaving'),

                html.H2(children='The weather is ...',
                style={'textAlign': 'left', 'color': 'black', 'fontSize': 20, 'font-family': font}),
                dcc.Checklist(['Rainy', 'Sunny', 'Cold', 'Warm'], id='weather'),

            ], style={'padding': 10, 'flex': 1, "border":"2px black solid"}),

            html.Br(),
            html.Div([
                html.H2(id='activity',
                style={'textAlign': 'center', 'color': 'black', 'fontSize': 30, 'font-family': font}),
            ], style={'padding': 10, 'flex': 1}),
            ], ),

        dcc.Tab(label = "Self care input",
                style={'color': 'black', 'fontSize': 20, 'font-family': font},
                    children=[
                html.H2(children='My preferred self-care activities',
                style={'textAlign': 'left', 'color': 'black', 'fontSize': 20, 'font-family': font}),
                dash_table.DataTable(
                    id='table-editing-simple',
                    columns=[
                        {'id': 'activity', 'name': 'activity'},
                        {'id': 'physical_energy', 'name': 'physical_energy', 'presentation': 'dropdown'},
                        {'id': 'mental_energy', 'name': 'mental_energy', 'presentation': 'dropdown'},
                        {'id': 'location', 'name': 'location', 'presentation': 'dropdown'},
                        {'id': 'leaving_house', 'name': 'Do I have to leave the house', 'presentation': 'dropdown'},
                    ],
                    editable=True,
                    dropdown={
                        'physical_energy': {
                            'options': [
                                ['low', 'medium', 'high']
                            ]
                        },
                        'mental_energy': {
                            'options': [
                                ['low', 'medium', 'high']
                            ]
                        },
                        'location': {
                            'options': [
                                ['inside', 'outside']
                            ]
                        },
                        'leaving_house': {
                            'options': [
                                ['Yes', 'No']
                            ]
                        }
                    },
                ),
                html.Div(id='table-dropdown-container')],),
        ],),
        ])

@callback(
    Output('activity', 'children'),
    [Input('physical', 'value'),
    Input('mental', 'value'),
    Input('leaving', 'value'),
    Input('weather', 'value')]
)

def activity_rec(physical, mental, leaving, weather):
    '''
        Function to extract activity that matches arguments
        :param physical: user input about physical energy
        :param mental: user input about mental energy
        :param weather: user input about the weather conditions
        :param leaving: user input about whether they want to leave the house or stay in
        :return: returns the activity that matches input
    '''
    if physical == 1 or 2:
        physical = 'Low'
    elif physical == 3:
        physical = 'Medium'
    else:
        physical = 'High'

    if mental == 1 or 2:
        mental = 'Low'
    elif mental == 3:
        mental = 'Medium'
    else:
        mental = 'High'

    if 'Rainy' in weather:
        location = 'Inside'
    else:
        location = 'Outside'

    requirements = [physical, mental, location, leaving]

    for index, row in df.iterrows():
        database = np.asarray(row[['Physical', 'Mental', 'Location', 'Leaving']])
        if np.array_equal(database, requirements):
            activity = row['Activity']
            return f'Activity is: {activity}'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)