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
weather = ['sunny']
leaving = 'Yes'

def activity_rec(physical, mental, weather, leaving):
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

    if 'rainy' in weather:
        location = 'Inside'
    else:
        location = 'Outside'
    print(location)
    requirements = [physical, mental, location, leaving]

    for index, row in df.iterrows():
        database = np.asarray(row[['Physical', 'Mental', 'Location', 'Leaving']])
        if np.array_equal(database, requirements):
            activity = row['Activity']
            return f'Activity is: {activity}'

activity_rec(physical, mental, weather, leaving)