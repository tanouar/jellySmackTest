import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

class JskDB:
    """
    Example of SQL connection class
    """
    
    def __init__(self):
        # MySQL database credentials 
        self.host = 'jellybas.cxvglcwgczps.us-west-2.rds.amazonaws.com'
        self.port = 3306
        self.user = 'da_ro' 
        self.password = 'UXDcu5ULheGEYJWF78Zy'
        self.db = 'da2'

    def create_connection(self):
        """Initialize MySQL connection"""
        engine = create_engine(f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}?charset=utf8",echo=False).connect()

        try:
            print(engine)
            return engine
        except Exception as e:
            print(e)


# How to use 
def my_function():
    """
    open a MySQL connection, run your code and close the connection
    """

    # open connection
    sql_connection = JskDB().create_connection()
    
    # My code to do something in MySQL Database
    
    # close connection
    sql_connection.close()