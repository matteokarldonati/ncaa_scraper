import pandas as pd
from bs4 import BeautifulSoup

from utils import get_request, parse_table, get_table_header


def get_espn_bpi(year):
    """
    :param year: string or int
    :return: pandas.DataFrame
    """
    base_url = "http://www.espn.com/mens-college-basketball/bpi/_/view/bpi/season/"

    data = []

    for i in range(1, 9):

        url = base_url + str(year) + '/page/' + str(i)

        r = get_request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"})

        if r is None:
            return data

        soup = BeautifulSoup(r.text, 'lxml')

        try:
            table = soup.find_all('table')[1]
        except:
            break

        data.extend(parse_table(table))

    columns = ['ranking'] + get_table_header(table, index=0)

    df = pd.DataFrame(data, columns=columns)

    return df
