import pandas as pd
from bs4 import BeautifulSoup

from utils import get_request


def get_sonny_moore_rating(year):
    """
    Scrape Sonny Moore's computer power index of a certain year
    :param year: string or int
    :return: pandas.DataFrame containing Sonny Moore’s ratings for a given year
    """
    # only the last two digits of the year are used in the url
    if len(str(year)) > 2:
        year = str(year)[-2:]

    url = 'http://sonnymoorepowerratings.com/cb' + str(year) + '.htm'

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"}

    r = get_request(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    header = soup.find_all('font')[1].text.split('\n')[1]
    columns = header.split()

    table = soup.find_all('b')[0]
    table = str(table.string)

    table = table.split('\n')
    data = []

    n = len(columns) - 1

    for i in table:
        row = i.split()
        if row:
            el = []
            name = ' '.join(row[1:-n])
            el.append(name)
            el.extend(row[-n:])
            data.append(el)

    df = pd.DataFrame(data=data, columns=columns)

    return df
