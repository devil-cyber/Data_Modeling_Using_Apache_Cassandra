import os 
import glob
import csv
import pandas as pd

def Preprocess_Data():
    value=['artist','firstName','gender','itemInSession','lastName','length',\
                'level','location','sessionId','song','userId'] 
    path = os.getcwd() + '/event_data'

    file_path_list = []
    for file in glob.glob(path+'/*.csv'):
        file_path_list.append(file)
    full_data_row = []
    for f in file_path_list:
        with open(f,'r',encoding='utf',newline='') as csv_file:
            csvreader = csv.reader(csv_file)
            next(csvreader)
            for line in csvreader:
                full_data_row.append(line)
    csv.register_dialect('myDialect',quoting=csv.QUOTE_ALL,skipinitialspace=True)
    with open('new_event_data.csv','w',encoding='utf',newline='') as f:
        writer = csv.writer(f,dialect='myDialect')
        writer.writerow(value)
        for row in full_data_row:
            if row[0]=='':
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
    df = pd.read_csv('new_event_data.csv')
    return df

Preprocess_Data()

