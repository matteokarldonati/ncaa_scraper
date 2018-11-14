import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from utils import get_request, parse_table, get_table_header


def get_schools_stats(year):
    """
    :param year: string or int
    :return: pandas.DataFrame containing statistics for each team for a given year
    """
    base_url = "https://www.sports-reference.com/cbb/seasons/"
    url = base_url + str(year) + '-school-stats.html'

    r = get_request(url, headers={"User-Agent": "Mozilla/5.0"})

    if r is None:
        return None

    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find_all('table')[0]

    data = parse_table(table)
    columns = get_table_header(table, index=1)

    df = pd.DataFrame(data, index=np.arange(1, len(data) + 1), columns=columns)

    df['NCAA'] = [el.endswith('NCAA') for el in df[df.columns[0]]]
    df[df.columns[0]] = df[df.columns[0]].str.replace('NCAA', '').str.strip()

    return df
