import pandas as pd
from sqlalchemy import create_engine
import time
from dotenv import load_dotenv
import os
load_dotenv()
class Database:
    def __init__(self):
        self.server = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_NAME')
        self.username = os.getenv('DB_USERNAME')
        self.password = os.getenv('DB_PASSWORD')
        # Connect to the database
        self.engine = create_engine(f'postgresql+psycopg2://{self.username}:{self.password}@{self.server}/{self.database}')
        self.connection = self.engine.connect()
    
    # Insert temperature, light, humidity data into the database
    def insert_data(self, temperature, light, humidity):
        current_time = pd.to_datetime(time.strftime("%Y-%m-%d %H:%M:%S"))
        data = {'time': [current_time], 'temperature': [temperature], 'light': [light], 'humidity': [humidity]}
        df = pd.DataFrame(data)
        # Insert DataFrame into the database table named 'data'
        df.to_sql('tmp_li_humi', self.engine, if_exists='append', index=False)
        print("Data inserted successfully.")
    
    #insert to table waterpump amount,name
    def insert_waterpump(self, amount, name):
        current_time = pd.to_datetime(time.strftime("%Y-%m-%d %H:%M:%S"))
        data = {'datetime': [current_time], 'amount': [amount], 'name': [name]}
        df = pd.DataFrame(data)
        # Insert DataFrame into the database table named 'waterpump2'
        df.to_sql('waterpump', self.engine, if_exists='append', index=False)
        print("Data inserted successfully.")
    
    #function to set last waterpump name to None
    def set_last_name(self):
        self.connection.execute(
            '''
            UPDATE waterpump
            SET name = 'None'
            WHERE datetime = (
                SELECT MAX(datetime)
                FROM waterpump
            );
            ''')
    


