import logging
from Log.Log import log_init
from Support.Exception import CheckCodeError
from Manager.Concept_Manager import Concept_Manager
inf=1



def Main():
    while inf!=0:
        input()
        print(1)
        try:
            Concept_Manager("1#1#1")
            pass
        except CheckCodeError:
            pass
    pass

if __name__=="__main__":
    log_init()
    logger = logging.getLogger("MainLogger")
    Main()