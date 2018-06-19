import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

num.plot.bar(y='win_proportion')
num.plot.bar(y='letality')


### ONLY ONE SIDE ###
mask1 = results['home_team'] == 'Mexico'
subset1 = results[mask1]
subset1 = difference(subset1)
subset1 = only_tournament(subset1, ['FIFA World Cup qualification',
    'FIFA World Cup'])
subset1.plot.line(y='difference', x = 'date')

subset1.rolling(4, win_type='triang').mean().plot.line(y='difference',
    x = 'date')

subset1.groupby('year').sum()

# Letality index (scores vs other score) -->
# Number of Games played -->
# Number of games won
# Number of games lost
# Ratio won / lost



mask2 = results['away_team'] == 'Mexico'
subset2 = results[mask2]




# mask = (results['home_team'] == 'Mexico') | (results['away_team'] == 'Mexico')
# set(results['tournament'])
