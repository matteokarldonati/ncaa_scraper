import requests
from lxml import html
import pandas as pd

def get_schools(year):
    """
    :param year: string
    :return: dataframe containing the names of the schools in alphabetical order
    """
    page = requests.get('https://www.sports-reference.com/cbb/seasons/' + str(year) + '-school-stats.html')
    tree = html.fromstring(page.content)
    schools = []

    for i in range(1, 500):  # 500 is more than the numbers of expected colleges
        try:
            a = tree.xpath('//*[@id="basic_school_stats"]/tbody/tr[' + str(i) + ']/td[1]/a')
            schools.append(a[0].get('href').split('/')[3])
        except:
            pass

    schools = pd.DataFrame(data = schools, columns = ['School_name'])
    return schools


print(get_schools(2018))
