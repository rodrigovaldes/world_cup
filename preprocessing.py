import pandas as pd
import numpy as np
import os

'''
This file creates the inputs for Fifa.Rmd file
'''

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
results = pd.read_csv("data/results.csv", parse_dates=['date'],
    date_parser=dateparse)

results['year'] = results['date'].map(lambda x: x.year)

results_aux = results.copy(deep=True)

results_aux.rename(columns= {'away_team': 'one', 'home_team': 'two',
    'away_score': 'score_1', 'home_score': 'score_2'}, inplace=True)

results.rename(columns= {'home_team': 'one', 'away_team': 'two',
    'home_score': 'score_1', 'away_score': 'score_2'}, inplace=True)

desired_order = ['date', 'one', 'two', 'score_1', 'score_2', 'tournament',
    'city', 'country', 'neutral', 'year']

results_aux = results_aux[desired_order]

results_all = pd.concat([results, results_aux])
results_all.sort_values(['date', 'one', 'two', 'score_1', 'score_2'],
    inplace = True)
results_all['win'] = results_all['score_1'] > results_all['score_2']
results_all.reset_index(drop=True, inplace = True)

results_all.to_csv('output/results_all.csv', index = None)

# Save a data frame with only the years of the FIFA worldcup
mask_wc = results_all['tournament'] == 'FIFA World Cup'
wc = results_all[['year']][mask_wc].drop_duplicates().reset_index(
    drop=True)
wc.to_csv('output/wc.csv', index = None)

# All countries who has gone to the World Cup
countries = sorted(list(set(
    results_all['one'][results_all['tournament'] == 'FIFA World Cup'])))

print(countries)
with open("output/countries.txt", "w") as file1:
    toFile = str(countries)
    file1.write(toFile)
