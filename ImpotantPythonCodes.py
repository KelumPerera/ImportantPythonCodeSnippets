
# Libraries that may usefull
import pandas as pd
from pandas import ExcelWriter
import numpy as np
from copy import deepcopy
import math
from time import time
import datetime
import re

# Load data from excel file
file = pd.read_excel(r"D:\path\to\file\All_Workings1.xlsx", sheet_name="Sheet1", skiprows=0, parse_dates=["DATE1","Date2"],dtype={ "StringColumn":'str'})

# Load data from CSV/txt file
file = pd.read_csv(r"\path\to\file\Cell_usage.txt",delimiter='|', names = ['Date','site Id','Cell ID','sitename','Duration Mins'] ,skiprows=0)

# Load data from fixt width txt file
file = pd.read_fwf(r"\path\to\file\Cell_usage.txt", names = ['Date','site Id','Cell ID','sitename','Duration Mins'] ,skiprows=0)

# Rename the columns
file = file.rename(columns={0: 'Date',1 : 'site Id',2 : 'Cell ID',3 : 'sitename', 4: 'Duration Mins'})

# Add a index column as a new column in the dataset
file = file.rename_axis('MY_Index').reset_index()

# Change the data types
#"Date" from object format to date format 
file['Date1']= pd.to_datetime(file['Date'])

# Delete a particular column
del file['Date']

# Change the "Duration Mins" column from object format to integer format
file['Duration Mins'] = pd.to_numeric(file['Duration Mins'], errors='coerce')

# Create a correct datatime format when the given data is in multiple datetime formats (first read the column as text)

def parse_datetime(date_string):
    formats = [
        '%d/%m/%Y %H:%M:%S',
        '%Y-%m-%d %H:%M:%S',
        '%d/%m/%Y %H:%M',
        '%m/%d/%Y %I:%M:%S %p',
        '%d/%m/%Y'
    ]
    for fmt in formats:
        try:
            return pd.to_datetime(date_string, format=fmt)
        except ValueError:
            continue
    raise ValueError("Unrecognized datetime format")

df["Initiated Date/Time "] = df["Initiated Date/Time "].apply(parse_datetime)


# Create a copy of the dataset 
file_BACKUP = deepcopy(file)


# How to drop specific column values using drop duplicates

df2 = pd.DataFrame({ 'ABC':['Second', 'Third', 'Third', 'Fourth', 'Fourth'],
                    'Name':['John', 'Tom', 'Tom', 'Tom','One'],
                    'Class':['Second', 'Third', 'Third', 'Fourth', 'Fourth'],
                    '123':['Second', 'Third', 'Third', 'Fourth', 'Fourth']
                    })


df2['Class1'] = df2['Class']
df2.insert(0, 'Class1', df2.pop('Class1'))
df2.insert(1, 'Class', df2.pop('Class'))

df2.iloc[:, 1:3] = df2.iloc[:, 1:3].drop_duplicates(['Class'],keep= "first")



# How to do a conditional group by sum

df2 = pd.DataFrame({ 'Name':['Second', 'Third', 'Third', 'Fourth', 'Fourth'],
                    'Sequance':['A100', 'A100', 'A100', 'B100','B100'],
                    'Class':['Second', 'Third', 'Third', 'Third', 'Fourth'],
                    'Amount':[100, 200, 300, 400, 500]
                    })

df2['Sq_wise_TotalValue'] = (df2.assign(Amount = df2['Value'].where((df2['Class'] != "Second") )).groupby(['Sequance'])['Amount'].transform('sum'))





# Create a list of dates as string values

from datetime import datetime
import pandas as pd
 
# start date
start_date = datetime.strptime("2023-03-01", "%Y-%m-%d")
end_date = datetime.strptime("2023-03-10", "%Y-%m-%d")
 
# difference between each date. D means one day
D = 'D'
 
date_list = pd.date_range(start_date, end_date, freq=D)
 
my_date_list_asStringElements= [date_obj.strftime('%Y-%m-%d') for date_obj in date_list]

# get count of unique records, assign sequence for similar records
df2 = pd.DataFrame({ 'Brand':['Second', 'Second', 'Second', 'Fourth', 'Fourth','Fourth','Fifth'],
                    'OutletID':['John', 'John', 'John', 'Tom','Tom','Tom','Tim'],
                    'Month':['Second', 'Second', 'Second', 'Fourth', 'Fourth','Fourth','Fifth'],
                    'SalesVolumes':[10, 10, 10, 5, 5,6,7],
                    'source_file':['10', '20', '10', '10', '20','60','70'],
                    'Ref':['Ref1', 'Ref2', 'Ref3', 'Ref4', 'Ref5', 'Ref6', 'Ref7']
                    })


df2["Record_count"] = df2.groupby(['Brand',"OutletID",'Month'])['Ref'].transform(lambda x: len(x.unique()))
df2["Grouped_volume"] = df2.groupby(['Brand',"OutletID",'Month'])["SalesVolumes"].transform('sum')

df2["Grouped_Filecount"] = df2.groupby(['Brand',"OutletID",'Month',"SalesVolumes"])["source_file"].transform(lambda x: len(x.unique()))

df2["Grouped_FileCumCount"] = df2.groupby(['Brand',"OutletID",'Month',"SalesVolumes"]).cumcount().add(1)

df2['Sequance'] = (~df2[['Brand',"OutletID",'Month',"SalesVolumes"]].duplicated()).cumsum()



# Read data from MS SQL server
from sqlalchemy import create_engine, text
import pyodbc

server = 'DESKTOP-UK769VU\SQLEXPRESS'  # Change to your SQL server name
driver = 'SQL+Server'
db = 'test'              # Change to your desired database name
un = 'username' 
pw = 'password'

engine = create_engine('mssql+pyodbc://{}/{}?driver={}'.format(server, db, driver))
engine1 = create_engine('mssql+pyodbc://{}:{}@{}/{}?driver={}'.format(un,pw,server, db, driver))

with engine.connect() as conn:
    test = pd.read_sql_query(text("select * from dbo.nlp_features_train"), conn)



# Search for whether a text file contain a text.
file = open(r"E:\filepath\part-file.csv",'r')
lines = file.readlines()
file.close()

lines_we_want = []

for i in range(len(lines)):
    if "my word to check" in lines[i]:
        lines_we_want.append(lines[i].strip("\n"))

print(lines_we_want)



# If you want to install a python package to a particular python version
# Change the command line directory to python installed folder

# cd C:\python3_12
# Then install the package

# python.exe -m pip install faker

