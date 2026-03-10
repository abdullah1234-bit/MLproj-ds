import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql



load_dotenv()

# use explicit names to avoid colliding with OS/user vars
host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
db=os.getenv('DB_NAME')



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df



    except Exception as ex:
        # include original exception and system info for debugging
        raise CustomException(ex, sys)
    


       

