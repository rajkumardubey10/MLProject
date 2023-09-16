import os
import sys
from src.mlproject.logger import logging 
from src.mlproject.exception import CustomException
import pandas as pd


from dataclasses import dataclass 


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifact', 'train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data_path:str=os.path.join('artifact','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingetion(self):
        try:
            ## reading the data from my sql
            logging.info("Reading from mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            

        except Exception as e:
            raise CustomException(e,sys)    