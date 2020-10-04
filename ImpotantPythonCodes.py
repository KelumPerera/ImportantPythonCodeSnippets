
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

# Create a copy of the dataset 
file_BACKUP = deepcopy(file)



