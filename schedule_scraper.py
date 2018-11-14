import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from utils import get_request, parse_table, get_table_header


def get_team_schedule(team, year):
    """
    :param team: string
    :param year: string or int
    :return: pandas.DataFrame containing the schedule of the team for the given year
    """
    base_url = "https://www.sports-reference.com/cbb/schools/"
    url = base_url + team + '/' + str(year) + '-schedule.html'

    r = get_request(url, headers={"User-Agent": "Mozilla/5.0"})

    if r is None:
        return None

    soup = BeautifulSoup(r.text, 'lxml')

    for caption in soup.find_all('caption'):
        if caption.get_text() == 'Schedule and Results Table':
            table = caption.find_parent('table')

    data = parse_table(table)
    columns = get_table_header(table)

    df = pd.DataFrame(data, index=np.arange(1, len(data) + 1), columns=columns)
    return df
