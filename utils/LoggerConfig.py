import logging


def log_config():
    logging.basicConfig(filename='treasure_hunters.log',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s: %(lineno)s - %(funcName)s() - '
                               '%(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')