from logger import logger
import os
import json


def chek_st_start() -> bool:
    return os.path.isdir(r'ARD WIN APPEREANCE CHANGER')

def st_start() -> bool:
    try:
        os.mkdir(r'ARD WIN APPEREANCE CHANGER')
        
    except Exception as exp:
        logger.error(exp)
