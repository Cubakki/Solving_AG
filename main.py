import logging
from Log.Log import log_init




def Main():
    log_init()
    logger=logging.getLogger("MainLogger")
    logger.debug("test")
    pass




if __name__=="__main__":
    Main()