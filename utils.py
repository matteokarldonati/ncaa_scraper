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
