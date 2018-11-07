import requests
from lxml import html

def get_school(year):
    '''
    :param year: year you want to get the list of schools from (can be either int or string)
    :return: list containing the names of the schools in alphqbetical order
    '''
    page = requests.get('https://www.sports-reference.com/cbb/seasons/'+str(year)+'-school-stats.html')
    tree = html.fromstring(page.content)
    hrefs = []

    for i in range(1,500): # 500 is more than the numbers of expected colleges
        try:
            a = tree.xpath('//*[@id="basic_school_stats"]/tbody/tr['+str(i)+']/td[1]/a')
            hrefs.append(a[0].get('href').split('/')[3])
        except:
            pass

    return hrefs
