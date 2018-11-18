import pandas as pd
import os

os.chdir('C:\\Users\\rdangelo\\Desktop\\ncaa_scraper\\data\\schedule')


def matches_populator(file):
    '''
    transform a csv into database entities

    :return: void function
    '''

    df = pd.read_csv(file)

    dn = pd.DataFrame(data=None,
                      columns=['Team_1', 'Team_2', 'Team_1_points', 'Team_2_points', 'OT', 'Winner', 'Neutral',
                               'Type', 'Arena', 'Date', 'Season'])

    dn['OT'] = [1 if x == 'OT' else 0 for x in df['OT']]
    dn['Neutral'] = [1 if x == 'N' else 0 for x in df[df.columns[3]]]
    dn['Type'] = df['Type'].values
    dn['Arena'] = df['Arena'].values
    dn['Date'] = df['Date'].values
    dn['Season'] = file.split('_')[0]

    # Now I pu in order team 1 and team 2 with the following logic: team 1 is the one at the
    for row in range(dn.shape[0]):
        if df[df.columns[3]].iloc[row] == '@':
            dn['Team_1'].iloc[row] = df['Opponent'].iloc[row]  ### BISOGNA PULIRLO E SOSTITUIRLO
            dn['Team_2'].iloc[row] = file.split('_')[1].replace('.csv', '') ### DA METTERE A POSTO
            dn['Team_1_points'].iloc[row] = df['Opp'].iloc[row]
            dn['Team_2_points'].iloc[row] = df['Tm'].iloc[row]
            dn['Winner'].iloc[row] = 0 if df[df.columns[6]].iloc[row] == 'W' else 1

        else:
            dn['Team_1'].iloc[row] = file.split('_')[1].replace('.csv', '') ### DA METTERE A POSTO
            dn['Team_2'].iloc[row] = df['Opponent'].iloc[row]  ### BISOGNA PULIRLO E SOSTITUIRLO
            dn['Team_1_points'].iloc[row] = df['Tm'].iloc[row]
            dn['Team_2_points'].iloc[row] = df['Opp'].iloc[row]
            dn['Winner'].iloc[row] = 1 if df[df.columns[6]].iloc[row] == 'W' else 0

    return dn


d = matches_populator('2006_akron.csv')

print(d)
