import os
import csv
from csv import reader
import pandas as pd
from datetime import datetime
import requests

def get_file_path(path):
    lst_of_files = []
    for filename in os.listdir(path):
        file = path + "/" + filename
        df = pd.read_csv(file).columns.tolist()
        if len(df) < 6:
            continue
        lst_of_files.append(df)
    return lst_of_files

def create_df(lst_of_files):
    col_names = ['title', 'year', 'president', 'content', 'url', 'footnote']
    df = pd.DataFrame(lst_of_files, columns=col_names) 
    print(df)
    # df.to_csv('/Users/Andey/Desktop/Fall2020/CIRP_Lab/farewell_addresses/farewell_speeches.csv')
    return None

def main():
    path = "/Users/Andey/Desktop/Fall2020/CIRP_Lab/farewell_addresses"
    lst_of_files = get_file_path(path)
    # print(lst_of_files)
    # create_df(lst_of_files)

if __name__ == "__main__":
    main()

