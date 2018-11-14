import logging
import time

import numpy as np

base_path = ""
folder = "/data"

logging.basicConfig(filename='logging.log', level=logging.INFO)


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

                if df is None:
                    logging.critical(str(param_1) + '_' + str(param_2))

                df.to_csv(base_path + folder + str(param_1) + '_' + str(param_2))

                logging.info(str(param_1) + '_' + str(param_2) + ' CREATED')

                wait = np.random.randint(10)
                time.sleep(wait)

    # if f has only one parameter
    else:
        for param in kwargs[list(kwargs.keys())[0]]:
            df = f(param)

            df.to_csv(base_path + folder + str(param))

            logging.info(str(param) + ' CREATED')

            wait = np.random.randint(10)
            time.sleep(wait)
