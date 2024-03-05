# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:12:05 2022

@author: Kelum desktop PC
"""

!pip install PyPDF2

import PyPDF2 as pdf

file = open(r'C:\Users\Kelum desktop PC\Downloads\alumex.pdf', 'rb')

file1 = open(r'C:\Users\Kelum desktop PC\Downloads\ASIAN HOTELS & PROPERTIES PLC.pdf', 'rb')


pdf_reader = pdf.PdfFileReader(file1)

last_page = pdf_reader.getNumPages()

a = pdf_reader.getPage(172).extractText()


start = page_content.find("REPORT ON THE AUDIT OF THE FINANCIAL STATEMENTS") + len("REPORT ON THE AUDIT OF THE FINANCIAL STATEMENTS")
end = page_content.find("Responsibilities of Management and Those Charged with Governance for the Financial Statements")
substring = page_content[start:end]
print(substring)


page_content=""                # define variable for using in loop.
for page_number in range(last_page):
    page = pdf_reader.getPage(page_number)
    page_content += page.extractText()     # concate reading pages.
  
 

