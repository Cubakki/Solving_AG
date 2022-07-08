import yaml
import logging.config
import os

def log_init():
    path = './Log/log_set.ymal'

    if os.path.exists(path):
        with open(path, "r") as f:
           config = yaml.load(f, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)

