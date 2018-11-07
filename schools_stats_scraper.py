import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# TO DO
# deal NCAA school name column


def get_schools_stats(year):
    """
    :param team: string
    :param year: string
    :return: pandas.DataFrame containing the schedule of the team for the given year
    """
    base_url = "https://www.sports-reference.com/cbb/seasons/"
    url = base_url + year + '-school-stats.html'

    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find_all('table')[0]

    table_rows = table.find_all('tr')

    th = table_rows[1].find_all('th')
    columns = [i.text for i in th][1:]

    data = []

    for tr in table_rows:
        td = tr.find_all('td')

        row = [i.text for i in td]

        if row:
            data.append(row)

    df = pd.DataFrame(data, index=np.arange(1, len(data) + 1), columns=columns)
    return df
