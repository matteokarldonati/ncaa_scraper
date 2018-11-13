import requests
from requests.exceptions import RequestException


def get_request(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"}):
    try:
        r = requests.get(url, timeout=timeout, headers=headers)
        if r.status_code == 200:
            return r
        else:
            print(r.status_code)  # add logging
            return None

    except RequestException as e:
        print(f'Error during requests to {url} : {str(e)}')  # add logging
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
