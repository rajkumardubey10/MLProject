import os
import sys
from src.mlproject.logger import logging 
from src.mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")


def read_sql_data():
    logging.info("Reading SQL Database started")
    try:
        logging.info("")
    except Exception as e:
        raise CustomException(e,sys)




