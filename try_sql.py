import os
import csv
import pandas as pd
from datetime import datetime
import requests
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

def sql_reader(path): 
    df = pd.read_csv(path)
    # print(df)
    df.to_sql('speeches', con=engine)
    print(engine.execute("SELECT * FROM speeches WHERE president = 'Donald J. Trump'").fetchall())

if __name__ == "__main__":
    path = '/Users/Andey/Desktop/Fall2020/CIRP_Lab/all_csv_files/all_presidents_cleaned copy.csv'
    df = sql_reader(path)




