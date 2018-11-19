import logging

import pandas as pd
import requests
from requests.exceptions import RequestException

logging.basicConfig(filename='logging.log', level=logging.INFO)


# SCRAPER UTILS


def get_request(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"}):
    try:
        r = requests.get(url, timeout=timeout, headers=headers)
        if r.status_code == 200:
            return r
        else:
            logging.error('STATUS CODE ' + str(r.status_code))
            return None

    except RequestException as e:
        logging.error(f'Error during requests to {url} : {str(e)}')
        return None


def parse_table(table):
    """
    :param table: html table
    :return: list of lists containing the data inside the table
    """
    table_rows = table.find_all('tr')

    data = []

    for tr in table_rows:
        td = tr.find_all('td')

        row = [i.text for i in td]

        if row:
            data.append(row)

    return data


def get_table_header(table, index=0):
    """
    :param table: html table
    :param index: int
    :return: list
    """
    table_rows = table.find_all('tr')

    th = table_rows[index].find_all('th')
    table_header = [i.text for i in th][1:]

    return table_header


# DB UTILS


def scores_table_csv_to_db(file_name, d_names):
    """
    transform a csv into database entities

    :return: void function
    """
    df = pd.read_csv(file_name)

    season = file_name.split('_')[0]
    team_1 = d_names[season][file_name.split('_')[1].replace('.csv', '')]

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
        team_2 = df['Opponent'].iloc[row]

        if team_2.endswith(')') and any(i.isdigit() for i in team_2.split('(')[-1]):
            team_2 = ''.join(team_2.split('(')[:-1]).strip()

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


def get_d_names():
    """
    :return: dictionary {year : {file_name : sport_reference_name}}
    """
    d = dict()

    for i in range(2000, 2001):
        df = pd.read_csv(str(i) + '.csv')

        d_names = dict()

        for index, row in df.iterrows():
            d_names[row['Link names']] = row['School']

        d[str(i)] = d_names

    return d
