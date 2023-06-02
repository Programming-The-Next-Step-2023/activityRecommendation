# App for Programming - The Next Step
# Fleur Korzilius
# May 2023

import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash import Dash, Output, Input, State, dcc, html, dash_table

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
external_stylesheets = [dbc.themes.MINTY, dbc_css]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "What should I do today?"

# import data from this dataframe for basic activity input
url = "https://raw.githubusercontent.com/Programming-The-Next-Step-2023/activityRecommendation/main/activities.csv"
df = pd.read_csv(url, sep=";", encoding="ISO-8859-1")

# tab 1 layout - recommends activity based on input
tab1_layout = html.Div(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    html.Div(
                                        [
                                            html.H2(children='Physical energy is ... (1 = very low, 5 = very high)',
                                                    style={'textAlign': 'left', 'fontSize': 17}),
                                            html.Div(dcc.Slider(1, 5, 1, value=1, id='physical'), style={'width':'80%'}),

                                            html.Br(),

                                            html.H2(children='Mental energy is ...(1 = very low, 5 = very high)',
                                            style={'textAlign': 'left', 'fontSize': 17}),
                                            html.Div(dcc.Slider(1, 5, 1, value=1, id='mental'), style={'width':'80%'}),

                                            html.Br(),

                                            html.H2(children='Do you want to leave the house?',
                                            style={'textAlign': 'left', 'fontSize': 17}),
                                            dcc.RadioItems(options=['Yes', 'No'], value='Yes', id='leaving'),

                                            html.Br(),
                                            html.Br()

                                        ]
                                    )
                                ],
                                style = {'paddingLeft': '50px'}),

                            dbc.Col(
                                children=[html.Div([
                                html.Br(),
                                html.H2(children='What is the weather like?',
                                style={'textAlign': 'left', 'fontSize': 17}),
                                dcc.RadioItems(
                                    [
                                        {
                                            "label":
                                                [html.Img(src="assets/rain.png", height=30),
                                                 html.Span("Rainy", style={'fontSize': 15, 'padding-left': 10}),],
                                            "value": "Rainy",
                                        },
                                        {
                                            "label":
                                                [html.Img(src="assets/cloud.png", height=30),
                                                 html.Span("Cloudy", style={'fontSize': 15, 'padding-left': 10}),],
                                            "value": "Cloudy",
                                        },
                                        {
                                            "label":
                                                [html.Img(src="assets/sun.png", height=30),
                                                 html.Span("Sunny", style={'fontSize': 15, 'padding-left': 10}),],
                                            "value": "Sunny",
                                        },
                                    ], id='rain', value='Rainy' , labelStyle={"display": "flex", "align-items": "center"},
                                ),

                                html.Br(),
                                html.H2(children='What is the temperature like?',
                                        style={'textAlign': 'left', 'fontSize': 17}),
                                dcc.RadioItems(options=[
                                    {
                                            "label":
                                                [html.Img(src="assets/warm.png", height=30),
                                                 html.Span("Warm", style={'fontSize': 15, 'padding-left': 10}),],
                                            "value": "Warm",
                                        },
                                        {
                                            "label":
                                                [html.Img(src="assets/cold.png", height=30),
                                                 html.Span("Cold", style={'fontSize': 15, 'padding-left': 10}),],
                                            "value": "Cold",
                                        },
                                ], value='Warm', id='temperature', inline=True),

                                html.Br(),
                                html.Br(),
                                dbc.Button('Submit', id='submit-button', n_clicks=0, style={'textAlign': 'center'}),
                                html.Br(),
                                html.Br()
                                ])
                            ],
                            style = {'paddingLeft': '50px'}), ]
                            ),

                                html.Div(children=[ # pop-up window that displays activity
                                    dbc.Modal(
                                        [dbc.ModalHeader(dbc.ModalTitle(id='activity')),
                                         dbc.ModalBody(html.Img(src="assets/selfcare.png", height=100),
                                                       style={'textAlign': 'center'}),
                                         ],
                                        id='modal',
                                        is_open=False,
                                        size='sm',
                                        centered=True),
                                ])
                ]
)

# tab 2 layout - for user input and removal of activities
tab2_layout = html.Div(
                children=[
                    html.Br(),
                    html.H2("My preferred self-care activities",
                    style={'textAlign': 'left', 'fontSize': 20}),
                    html.Br(),

                    # convert original dataframe to datatable and make it editable for user input
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

                        dropdown = { # dropdown options are based on all unique values in the original dataframe for that column
                        'Physical': {
                            'options': [{'label': str(i), 'value': str(i)}
                                for i in df['Physical'].unique()]
                        },
                        'Mental': {
                            'options': [{'label': str(i), 'value': str(i)}
                                for i in df['Mental'].unique()]
                        },
                        'Location': {
                            'options': [{'label': i, 'value': i}
                                for i in df['Location'].unique()]
                        },
                        'Leaving': {
                            'options': [{'label': i, 'value': i}
                                for i in df['Leaving'].unique()]
                        }
                    },
                    ),

                    dbc.Button('Add Activity', id='editing_rows', n_clicks=0), # to add row to datatable
                    dbc.Button('Submit', id='submit-button2', n_clicks=0), # to save the updated datatable for use in tab 1
                    dcc.Store(id='input-store')
                ]
)

app.layout = html.Div([
    html.Br(),
    html.H1(children='What should I do today?', style={'textAlign': 'center', 'fontSize': 30}),
    html.Br(),

    dcc.Tabs([
        dcc.Tab(label = "How do I feel?", children= tab1_layout, style={'fontSize': 20}),

        dcc.Tab(label = "Self-care activity input", children= tab2_layout, style={'fontSize': 20})
    ])
])

## Callbacks tab 1
@app.callback(
    Output('activity', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('physical', 'value'),
    State('mental', 'value'),
    State('leaving', 'value'),
    State('rain', 'value'),
    State('temperature', 'value'),
    State('input_activities_table', 'data')]
)

def activity_rec(n_clicks, physical, mental, leaving, rain, temperature, input_data):
        '''
            Function to extract activity that matches arguments
            :param n_clicks: to see whether user has filled in all information
            :param physical: user input about physical energy (range 1:5)
            :param mental: user input about mental energy (1:5)
            :param leaving: user input about whether they want to leave the house or stay in
            :param rain: user input about the weather conditions
            :param temperature: user input about the weather conditions
            :param input_data: datatable from tab 2
            :return: returns the activity that matches input
        '''
        if n_clicks is not None and n_clicks > 0:
            # everytime user clicks submit button, function starts running

            df_input = pd.DataFrame(input_data) # use dataframe from tab 2

            if rain == 'Rainy':
                location = 'Inside'
            elif temperature == 'Cold' and rain == 'Cloudy':
                location = 'Inside'
            else:
                location = 'Outside'
                # if weather is rainy or cold and cloudy activity is inside, otherwise activity is outside

            activity = 'Error: No activities match your state' # return statement if no activity in database is equal to input
            requirements = np.array([physical, mental, location, leaving], dtype=object) # input in array form

            # shuffle the rows of df_input to randomize the loop
            df_input = df_input.sample(frac=1).reset_index(drop=True)

            for index, row in df_input.iterrows():
                database = np.asarray(row[['Physical', 'Mental', 'Location', 'Leaving']])
                if np.array_equal(database, requirements):
                    activity = row['Activity']
                    #if requirements and the row that is being looped over are equal, then activity gets saved

            return f'{activity}'

@app.callback(
    Output('modal', 'is_open'),
    [Input('submit-button', 'n_clicks')],
    [State('modal', 'is_open')],
)
def activity_modal(n_clicks, is_open):
    '''
    :param n_clicks: nr of clicks on submit button
    :param is_open: keeps track of presence of a pop-up window
    :return: when submit button is clicked, a window pops up with the activity
    '''
    if n_clicks:
        return not is_open
    return is_open

# Callbacks tab 2
@app.callback(
    Output('input_activities_table', 'data'),
    [Input('editing_rows', 'n_clicks')],
    [State('input_activities_table', 'data'),
    State('input_activities_table', 'columns')])

def add_row(n_clicks, rows, columns):
    '''
       :param n_clicks: nr of clicks on add activity button
       :param rows: rows of datatable
       :param columns: columns of datatable
       :return: new row gets added when button is clicked
    '''
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows

@app.callback(
    Output('input-store', 'data'),
    Input('submit-button2', 'n_clicks'),
    State('input_activities_table', 'data')
)

def update_database(n_clicks, input_data):
    '''
    :param n_clicks: nr of clicks on submit button
    :param input_data: datatable with activities
    :return: once submit button is clicked, the datatable gets saved and will be used as database in tab 1
    '''
    if n_clicks is not None and n_clicks > 0:
        return input_data



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)