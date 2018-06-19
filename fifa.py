import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
-------------------------------------------------------------------------------
This part of the code is not neccesary for the final product.

This is an exploratory file. I replicate most of this inside the code in R
-------------------------------------------------------------------------------
'''

def only_tournament(df, t = ['FIFA World Cup']):

    mask = df['tournament'].isin(t)
    df = df[mask]
    df.reset_index(drop=True, inplace=True)
    return df

def difference(df, team = 'home_score'):
    '''
    '''
    if team == 'home_score':
        df['difference'] = df['home_score'] - df['away_score']
    else:
        df['difference'] = df['away_score'] - df['home_score']

    df.reset_index(drop=True, inplace=True)
    return df

results_all = pd.read_csv('output/results_all.csv')

### COMPILATION HOME AND AWAY ###
subset1_all = results_all[results_all['one'] == 'Mexico'].reset_index(drop=True)
subset1_all = only_tournament(subset1_all, ['FIFA World Cup'])

## Number of games played
num_play = subset1_all[['score_1', 'year']].groupby(['year']).count().rename(
    columns = {'score_1': 'matches'})
num_win = subset1_all.groupby(['year']).sum()
num = num_play.merge(num_win, left_index=True, right_index=True)
num['letality'] = num['score_1'] / num['score_2']
num['win_proportion'] = num['win'] / num['matches']
