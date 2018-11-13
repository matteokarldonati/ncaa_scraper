import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from utils import get_request, parse_table, get_table_header


def get_ken_pomeroys_rating(year):
    """
    :param year: string or int
    :return: pandas.DataFrame containing Ken Pomeroy’s ratings for a given year
    """
    base_url = "https://kenpom.com/index.php?y="
    url = base_url + str(year)

    r = get_request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"})

    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.find_all('table')[0]

    data = parse_table(table)
    columns = get_table_header(table, index=1)

    data = np.array(data)
    cleaned_data = []

    for i in data:
        mask = [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19]

        cleaned_data.append(i[mask])

    df = pd.DataFrame(cleaned_data, index=np.arange(1, len(data) + 1), columns=columns)

    return df
