import logging
import time

import numpy as np

logging.basicConfig(filename='logging.log', level=logging.INFO, filemode="w")


def scraper(f, params, wait_range=(1, 10)):
    """
    General template for scraping

    :param f: scraping function
    :param params: list of list containing the parameters to be passed to the scraping function
    :param wait_range: tuple
    :return: None
    """
    if len(params) == 1:
        for param in params[0]:
            df = f(param)

            if df is None:
                logging.critical(str(param))
                continue

            df.to_csv(str(param) + '.csv')

            logging.info(str(param) + ' CREATED')

            wait = np.random.randint(*wait_range)
            time.sleep(wait)

    elif len(params) == 2:
        for param_1 in params[0]:
            for param_2 in params[1]:
                df = f(param_1, param_2)

                if df is None:
                    logging.critical(str(param_1) + '_' + str(param_2))
                    continue

                df.to_csv(str(param_1) + '_' + str(param_2) + '.csv')

                logging.info(str(param_1) + '_' + str(param_2) + ' CREATED')

                wait = np.random.randint(*wait_range)
                time.sleep(wait)
    else:
        raise Exception("Invalid input params")

    logging.info('DONE')
