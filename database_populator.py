import pandas as pd


def matches_populator(file_name):
    """
    transform a csv into database entities

    :return: void function
    """
    df = pd.read_csv(file_name)

    team_1 = file_name.split('_')[1].replace('.csv', '')  # da mettere a posto
    season = file_name.split('_')[0]

    table = pd.DataFrame(data=None,
                         columns=['Team_1', 'Team_2', 'Team_1_points', 'Team_2_points', 'OT', 'Winner', 'Neutral',
                                  'Type', 'Arena', 'Date', 'Season'])

    table['OT'] = [1 if x == 'OT' else 0 for x in df['OT']]
    table['Neutral'] = [1 if x == 'N' else 0 for x in df[df.columns[3]]]
    table['Type'] = df['Type'].values
    table['Arena'] = df['Arena'].values
    table['Date'] = df['Date'].values
    table['Season'] = season

    # reorder team_1 and team_2 with the following logic: team 1 is the home team
    # if the game was played on a neutral court, the names are ordered alphabetically
    for row in range(table.shape[0]):
        symbol = df[df.columns[3]].iloc[row]
        team_2 = df['Opponent'].iloc[row]  # da pulire e sostituire
        if symbol == '@':
            table['Team_1'].iloc[row] = team_2
            table['Team_2'].iloc[row] = team_1
            table['Team_1_points'].iloc[row] = df['Opp'].iloc[row]
            table['Team_2_points'].iloc[row] = df['Tm'].iloc[row]
            table['Winner'].iloc[row] = 0 if df[df.columns[6]].iloc[row] == 'W' else 1

        elif symbol == 'N':
            if team_1 < team_2:
                table['Team_1'].iloc[row] = team_1
                table['Team_2'].iloc[row] = team_2
                table['Team_1_points'].iloc[row] = df['Tm'].iloc[row]
                table['Team_2_points'].iloc[row] = df['Opp'].iloc[row]
                table['Winner'].iloc[row] = 1 if df[df.columns[6]].iloc[row] == 'W' else 0
            else:
                table['Team_1'].iloc[row] = team_2
                table['Team_2'].iloc[row] = team_1
                table['Team_1_points'].iloc[row] = df['Opp'].iloc[row]
                table['Team_2_points'].iloc[row] = df['Tm'].iloc[row]
                table['Winner'].iloc[row] = 0 if df[df.columns[6]].iloc[row] == 'W' else 1

        else:
            table['Team_1'].iloc[row] = team_1
            table['Team_2'].iloc[row] = team_2
            table['Team_1_points'].iloc[row] = df['Tm'].iloc[row]
            table['Team_2_points'].iloc[row] = df['Opp'].iloc[row]
            table['Winner'].iloc[row] = 1 if df[df.columns[6]].iloc[row] == 'W' else 0

    return table
