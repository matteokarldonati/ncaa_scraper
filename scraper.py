import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_team_schedule(team, year):
    base_url = "https://www.sports-reference.com/cbb/schools/"
    url = base_url + team + '/' + year + '-schedule.html'

    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    soup = BeautifulSoup(r.text, 'lxml')

    for caption in soup.find_all('caption'):
        if caption.get_text() == 'Schedule and Results Table':
            table = caption.find_parent('table')

    table_rows = table.find_all('tr')

    th = table_rows[0].find_all('th')
    columns = [i.text for i in th][1:]

    data = []

    for tr in table_rows:
        td = tr.find_all('td')

        row = [i.text for i in td]

        if row:
            data.append(row)

    df = pd.DataFrame(data, index=np.arange(1, len(data) + 1), columns=columns)
    return df
