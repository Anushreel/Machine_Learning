import os
import sys
from src.logger import logging
from src.exception import CustomException
import dill

from sklearn.metrics import r2_score

def save_obj(file_path:str, obj) -> None:
    ''' save the given object in the given file path '''
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
        logging.info('Object saved successfully')
    except Exception as e:
        logging.info('!!! Error occured in save object')
        raise CustomException(e, sys)
    
def load_obj(file_path:str):
    ''' loads the object from the given file path '''
    try:
        with open(file_path, 'rb') as file:
            obj = dill.load(file)
        logging.info('Object loaded successfully')
        return obj
    except Exception as e:
        logging.info('!!! Error occured in loading object')
        raise CustomException(e, sys)