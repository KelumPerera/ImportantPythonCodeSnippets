# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:18:09 2017

@author: Kelum Perera
"""
# Excel files
import glob
import pandas as pd
from pandas import ExcelWriter

# Define the path to folder contained excel files to combine/merge
path = "C:/Users/yourname/folder/path"
file_identifier = "*.xlsx"

#Mearge excel files into a pandas dataframe
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



#CSV files
import glob
import pandas as pd

# Define the path to folder contained CSV files to combine/merge
path = "C:/Users/yourname/folder/path"
file_identifier = "*.csv"   # If these are text files use "*.txt"

#Mearge CSV files into a pandas dataframe
merged_csv = pd.DataFrame()
for f in glob.glob(path + "/*" + file_identifier):
    df = pd.read_csv(f)
    merged_csv = merged_csv.append(df,ignore_index=True)

# Write the data frame to a CSV file.
merged_CSV.to_csv('C:/Users/yourname/folder/Combinedfile.csv', sep='\t', encoding='utf-8', index=False)
