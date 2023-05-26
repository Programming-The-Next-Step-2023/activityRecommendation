# App for Programming - The Next Step
# Fleur Korzilius
# May 2023

import pandas as pd
import numpy as np
from dash import Dash, callback, Output, Input, State, dcc, html, dash_table, dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "What should I do?"

# import data from this dataframe for basic activity input
df = pd.read_csv(r'C:\Research Master Psychology UVA\Semester IV\Programming - The Next Step\activities.csv', encoding="ISO-8859-1", sep=";")
font = 'monospace'

# tab 1 layout
tab1_layout = html.Div(
                children=[
                    html.Div([
                    html.H2(children='Physical energy is ... (1 = very low, 5 = very high)',
                            style={'textAlign': 'left', 'color': 'black', 'fontSize': 17, 'font-family': font}),
                    dcc.Slider(1, 5, 1, value=1, id='physical'),

                    html.H2(children='Mental energy is ...(1 = very low, 5 = very high)',
                    style={'textAlign': 'left', 'color': 'black', 'fontSize': 17, 'font-family': font}),
                    dcc.Slider(1, 5, 1, value=1, id='mental'),

                    html.H2(children='Do you want to leave the house?',
                    style={'textAlign': 'left', 'color': 'black', 'fontSize': 17, 'font-family': font}),
                    dcc.RadioItems(options=['Yes', 'No'], value='Yes', id='leaving'),
                    ], style={'width': '49%','display':'inline-block'}),

                    html.Div([
                        html.H2(children='What is the weather like?',
                        style={'textAlign': 'left', 'color': 'black', 'fontSize': 17, 'font-family': font}),
                        dcc.RadioItems(
                            [
                                {
                                    "label":
                                        [
                                            html.Img(src="/assets/rain.png", height=30),
                                            html.Span("Rainy", style={'font-size': 15, 'padding-left': 10}),
                                        ],
                                    "value": "Rainy",
                                },
                                {
                                    "label":
                                        [
                                            html.Img(src="/assets/cloud.png", height=30),
                                            html.Span("Cloudy", style={'font-size': 15, 'padding-left': 10}),
                                        ],
                                    "value": "Cloudy",
                                },
                                {
                                    "label":
                                        [
                                            html.Img(src="/assets/sun.png", height=30),
                                            html.Span("Sunny", style={'font-size': 15, 'padding-left': 10}),
                                        ],
                                    "value": "Sunny",
                                },
                            ], id='rain', value='Rainy' , labelStyle={"display": "flex", "align-items": "center"},
                        ),

                        html.H2(children='What is the temperature like?',
                        style={'textAlign': 'left', 'color': 'black', 'fontSize': 17, 'font-family': font}),
                        dcc.RadioItems(options=[
                            {
                                    "label":
                                        [
                                            html.Img(src="/assets/warm.png", height=30),
                                            html.Span("Warm", style={'font-size': 15, 'padding-left': 10}),
                                        ],
                                    "value": "Warm",
                                },
                                {
                                    "label":
                                        [
                                            html.Img(src="/assets/cold.png", height=30),
                                            html.Span("Cold", style={'font-size': 15, 'padding-left': 10}),
                                        ],
                                    "value": "Cold",
                                },
                        ], value='Warm', id='temperature', inline=True),

                        html.Br(),
                        html.Br(),
                        html.Button('Submit', id='submit-button', n_clicks=0,
                                    style={'textAlign': 'center'})

                    ], style={'width': '50%','display':'inline-block'}),

                    html.Div(children=[

                        html.H2(id='activity',
                        style={'textAlign': 'center', 'color': 'black', 'fontSize': 30, 'font-family': font, 'border':'1px red solid'}),
                    ],),
                ],)
# tab 2 layout
# this tab allows user to input own activities and remove activities that they do not want to be recommended
tab2_layout = html.Div(
                children=[
                    html.H2(children='My preferred self-care activities',
                    style={'textAlign': 'left', 'color': 'black', 'fontSize': 20, 'font-family': font}),

                    dash_table.DataTable(
                        id='input_activities_table',
                        data=df.to_dict('records'),
                        columns=[
                            {'name': 'Activity', 'id': 'Activity', 'editable': True, 'presentation': 'input'},
                            {'name': 'Physical energy input', 'id': 'Physical', 'editable': True, 'presentation': 'dropdown'},
                            {'name': 'Mental energy input', 'id': 'Mental', 'editable': True, 'presentation': 'dropdown'},
                            {'name': 'Location', 'id': 'Location', 'editable': True, 'presentation': 'dropdown'},
                            {'name': 'Do you have to leave the house?', 'id': 'Leaving', 'editable': True, 'presentation': 'dropdown'}
                        ],
                        editable=True,
                        row_deletable=True,

                        dropdown = {
                        'Physical': {
                            'options': [
                                {'label': str(i), 'value': str(i)}
                                for i in df['Physical'].unique()
                            ]
                        },
                        'Mental': {
                            'options': [
                                {'label': str(i), 'value': str(i)}
                                for i in df['Mental'].unique()
                            ]
                        },
                        'Location': {
                            'options': [
                                {'label': i, 'value': i}
                                for i in df['Location'].unique()
                            ]
                        },
                        'Leaving': {
                            'options': [
                                {'label': i, 'value': i}
                                for i in df['Leaving'].unique()
                            ]
                        }
                    },
                    ),
                    html.Div(id='table-dropdown-container'),
                    html.Button('Add Activity', id='editing_rows', n_clicks=0),
                    html.Button('Submit', id='submit-button2', n_clicks=0),
                    dcc.Store(id='input-store')
                        ])





app.layout = html.Div([
    html.H1(children='What should I do today?',
            style={'textAlign': 'center', 'color': 'black', 'fontSize': 30, 'font-family': font}),

    dcc.Tabs([
        dcc.Tab(label = "How do I feel?", children= tab1_layout,
                style={'color': 'black', 'fontSize': 20, 'font-family': font}),

        dcc.Tab(label = "Self-care activity input", children= tab2_layout,
                style={'color': 'black', 'fontSize': 20, 'font-family': font})
            ]),
])

@app.callback(
    Output('activity', 'children'),
    [Input('submit-button', 'n_clicks'),
    Input('physical', 'value'),
    Input('mental', 'value'),
    Input('leaving', 'value'),
    Input('rain', 'value'),
    Input('temperature', 'value')]
)

def activity_rec(n_clicks, physical, mental, leaving, rain, temperature):
        '''
            Function to extract activity that matches arguments
            :param n_clicks: to see whether user has filled in all information
            :param physical: user input about physical energy (range 1:5)
            :param mental: user input about mental energy (1:5)
            :param leaving: user input about whether they want to leave the house or stay in
            :param rain: user input about the weather conditions
            :param temperature: user input about the weather conditions
            :return: returns the activity that matches input
        '''

        if n_clicks > 0:
            # if user clicks submit button, function starts running

            if rain == 'Rainy':
                location = 'Inside'
            elif temperature == 'Cold' and rain == 'Cloudy':
                location = 'Inside'
            else:
                location = 'Outside'

            activity = 'Error: No activities match your state'
            requirements = np.array([physical, mental, location, leaving], dtype=object)

            for index, row in df.iterrows():
                database = np.asarray(row[['Physical', 'Mental', 'Location', 'Leaving']])
                if np.array_equal(database, requirements):
                    activity = row['Activity']
                    #if requirements and the row that is being looped over are equal, then activity gets saved

            return f'{activity}'

@app.callback(
    Output('input_activities_table', 'data'),
    [Input('editing_rows', 'n_clicks')],
    [State('input_activities_table', 'data'),
    State('input_activities_table', 'columns')])

def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows







# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)