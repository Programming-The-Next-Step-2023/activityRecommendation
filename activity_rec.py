# App for Programming - The Next Step
# Fleur Korzilius
# May 2023

import pandas as pd
import numpy as np

# dataframe to compare with
df = pd.read_csv(r'C:\Research Master Psychology UVA\Semester IV\Programming - The Next Step\activities.csv', encoding="ISO-8859-1", sep=";")

# values to test function
physical = 1
mental = 1
leaving = 'Yes'
rain = 'Rainy'
temperature = 'Warm'
n_clicks = 1


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

        return f'{activity}'


activity_rec(physical, mental, leaving, rain, temperature, n_clicks)