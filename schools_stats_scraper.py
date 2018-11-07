import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

from utils import parse_table, get_table_header

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

    data = parse_table(table)
    columns = get_table_header(table, index=1)

    df = pd.DataFrame(data, index=np.arange(1, len(data) + 1), columns=columns)
    return df
