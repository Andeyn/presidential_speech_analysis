import os
import csv
import pandas as pd

def write_csv(df):
    new_path = '/Users/Andey/Desktop/Fall2020/uni_all_presidential_speeches.csv'
    df.to_csv(new_path,encoding='utf-8-sig',index=True)


def removeQ_A(path): #remove Q_A,
    df = pd.read_csv(path)
    print(df)
    dropLst = []
    for index, row in df.iterrows():
        dropLst.append(index)
        print(index)
        break
        try:
            if(len(row['CONTENT'])) < 10 or row['CONTENT'].find('Q. ') != -1:
                dropLst.append(index)
        except TypeError:
            dropLst.append(index)
    dropLst.pop()
    dropLst.pop()
    for i in dropLst:
        df = df.drop(index=i)
    keep_col =  ['SPEECH_ID', 'TITLE', 'DATE', 'YEAR', 'PRESIDENT', 'PRESIDENT_ID', 'CONTENT', 'URL', 'FOOTNOTE', 'SPEECH_TYPE']
    df = df[keep_col]
    return df


if __name__ == "__main__":
    path = '/Users/Andey/Desktop/Fall2020/CIRP_Lab/jupyter/all_presidential_speeches.csv'
    df = removeQ_A(path)
    write_csv(df)