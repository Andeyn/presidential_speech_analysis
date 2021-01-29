import os
import csv
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def removeQ_A(path): #remove Q_A,
    df = pd.read_csv(path)
    for index, row in df.iterrows():
        print(row['content'])
        break

if __name__ == "__main__":
    path = '/Users/Andey/Desktop/Fall2020/CIRP_Lab/all_csv_files/all_presidents_cleaned copy.csv'
    df = removeQ_A(path)