# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:18:09 2017
Code: Combines similer CSV or excel files using python 
@author: Kelum Perera
"""

import glob
import pandas as pd
from pandas import ExcelWriter

# Excel files
# Define the path to folder contained excel files to combine/merge
path = "C:/Users/yourname/folder/path"
file_identifier = "*.xlsx"

#Merge excel files into a pandas dataframe
merged_data = pd.DataFrame()
for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_excel(f)
    merged_data = merged_data.append(df,ignore_index=True)

# Write the data frame to a excel sheet.
writer = ExcelWriter('C:/Users/yourname/folder/Combinedfile.xlx')
merged_data.to_excel(writer,'Sheet1',index=False)
writer.save()

# Write the data frame to a CSV file.
merged_data.to_csv('C:/Users/yourname/folder/Combinedfile.csv', sep='\t', encoding='utf-8', index=False)



#CSV (Comma Separated Value) files
import glob
import pandas as pd

# Define the path to folder contained CSV files to combine/merge
path = "C:/Users/yourname/folder/path"
file_identifier = "*.csv"   # If your files are text files(Values separated by Tab) use "*.txt" or (Values separated by pip (|) use ".pip" 

#Merge CSV files into a pandas dataframe
merged_csv = pd.DataFrame()
for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_csv(f)
    merged_csv = merged_csv.append(df,ignore_index=True)

# Write the data frame to a CSV file.
merged_CSV.to_csv('C:/Users/yourname/folder/Combinedfile.csv', sep='\t', encoding='utf-8', index=False)


# Excel file with many similar sheets
# Define the path to the excel file which has many similar sheets to combine/merge
pathToExcelFile = "C:/Users/yourname/folder/path/Myfile.xlsx"

# Load spreadsheet
xl = pd.ExcelFile(excelFile)

# Load the worksheet names
worksheets = xl.sheet_names

#Merge excel worksheets into a pandas dataframe
merged_data = pd.DataFrame()
for ws in worksheets:
    df = pd.read_excel(pathToExcelFile, sheetname=ws, skiprows=0) # Skip some number of rows in excel sheets if required
    merged_data = merged_data.append(df,ignore_index=True)

# Write the data frame to a excel sheet.
writer = ExcelWriter('C:/Users/yourname/folder/Combinedfile.xlx')
merged_data.to_excel(writer,'Sheet1',index=False)
writer.save()

# Write the data frame to a CSV file.
merged_data.to_csv('C:/Users/yourname/folder/Combinedfile.csv', sep='\t', encoding='utf-8', index=False)




# Read a particular named worksheets in each excel work books in a given folder
# Write to a CSV files one by one

import glob
import pandas as pd

# Excel files
# Define the path to folder contained excel files to combine/merge
path = "C:/Users/yourname/folder/path"
file_identifier = "*.xlsx"
ws = "GL"

#Raed particular worksheet in each excel file and save into CSV files
df = pd.DataFrame()
for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_excel(f,sheetname=ws)
    writer = (f+".csv")
    df.to_csv(writer, sep='\t', encoding='utf-8', index=False)
