# App for Programming - The Next Step
# Fleur Korzilius
# May 2023

import pandas as pd
import numpy as np

# dataframe to compare with
url = "https://raw.githubusercontent.com/Programming-The-Next-Step-2023/activityRecommendation/main/activities.csv"
df = pd.read_csv(url, sep=";", encoding="ISO-8859-1")

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

        df_input = pd.DataFrame(input_data)  # use dataframe from tab 2

        if rain == 'Rainy':
            location = 'Inside'
        elif temperature == 'Cold' and rain == 'Cloudy':
            location = 'Inside'
        else:
            location = 'Outside'
            # if weather is rainy or cold and cloudy activity is inside, otherwise activity is outside

        activity = 'Error: No activities match your state'  # return statement if no activity in database is equal to input
        requirements = np.array([physical, mental, location, leaving], dtype=object)  # input in array form

        # shuffle the rows of df_input to randomize the loop
        df_input = df_input.sample(frac=1).reset_index(drop=True)

        for index, row in df_input.iterrows():
            database = np.asarray(row[['Physical', 'Mental', 'Location', 'Leaving']])
            if np.array_equal(database, requirements):
                activity = row['Activity']
                # if requirements and the row that is being looped over are equal, then activity gets saved

        return f'{activity}'

