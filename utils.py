import requests
import logging
from requests.exceptions import RequestException

logging.basicConfig(filename='logging.log', level=logging.INFO)

def get_request(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"}):
    try:
        r = requests.get(url, timeout=timeout, headers=headers)
        if r.status_code == 200:
            logging.info('Connected')
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
