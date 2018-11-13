import time

import numpy as np

base_path = ""
folder = "/data"


def scraper(f, **kwargs):
    """
    General template for scraping

    :param f: scraping function
    :param kwargs: arguments of the scraping function
    :return: None
    """

    # if f has 2 parameters
    if len(list(kwargs.keys())) > 1:
        for param_1 in kwargs[list(kwargs.keys())[0]]:
            for param_2 in kwargs[list(kwargs.keys())[1]]:
                df = f(param_1, param_2)

                df.to_csv(base_path + folder + str(param_1) + '_' + str(param_2))

                time.sleep(np.random.randint(10))

    # if f has only one parameter
    else:
        for param in kwargs[list(kwargs.keys())[0]]:
            df = f(param)

            df.to_csv(base_path + folder + str(param))

            time.sleep(np.random.randint(10))
