import time
import numpy as np
from schools_stats_scraper import get_schools_stats
from schedule_scraper import get_team_schedule

def scraper(f, **kwargs):
    '''
    General template for scraping

    :param f: scraping function
    :param kwargs: arguments of the scraping function
    :return: None
    '''

    # if f has 2 parameters
    if len(list(kwargs.keys())) > 1:
        for param_1 in kwargs[list(kwargs.keys())[0]]:
            for param_2 in kwargs[list(kwargs.keys())[1]]:
                d = f(param_1, param_2)
                d.to_csv(str(param_1)+'_'+ str(param_2) + '.csv')
                time.sleep(np.random.randint(10))

    # if f has only one parameter
    else:
        for param in kwargs[list(kwargs.keys())[0]]:
            d = f(param)
            d.to_csv(str(param) + '.csv')
            time.sleep(np.random.randint(10))
