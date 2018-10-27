# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:51:45 2018

Purpose- Extract email data from .msg files that are saved in a puticular location 

@author: Kelum Perera
"""

import ExtractMsg
import glob
import pandas as pd
from pandas import ExcelWriter

#Extract data from email (.msg) files into a pandas dataframe

# Input/Output the file path details
path = "C:/Users/kelum/Documents/EmailTest/"  # Input your file path
input_file_identifier = "*.msg"
output_file = "AllEmailData.xlsx"

f = glob.glob(path + "/*" + input_file_identifier)

# Otherwise use
# f = glob.glob(r'C:\Users\kelum\Documents\EmailTest\*.msg')

# Create an emplty dataframe
emailcolumns=['Msg_Sender','Msg_Date','Msg_To','Msg_CC','Msg_Attachments','Msg_Subj','Msg_Body']
email_data = pd.DataFrame(columns=emailcolumns)

# For loop to extract data from the emails in the defined path and insert into empty dataframe
for filename in f:
    msg = ExtractMsg.Message(filename)
    msg_sender = msg.sender
    msg_date = msg.date
    msg_To = msg.to
    msg_CC = msg.cc
    msg_Attachments = msg.attachments
    msg_subj = msg.subject
    msg_message = msg.body
    msg_List =[[msg_sender,msg_date,msg_To,msg_CC,msg_Attachments,msg_subj,msg_message]]
    email_data1 = pd.DataFrame(msg_List,columns=emailcolumns)
    email_data = email_data.append(email_data1,ignore_index=True)

# Write the dataframe into a excel worksheet.
writer = ExcelWriter(path + output_file)
email_data.to_excel(writer,'Sheet1',index=True)
writer.save()