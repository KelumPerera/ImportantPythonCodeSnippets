# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:26:08 2021

Example python code on how to find the minimum number of notes of different denominations that sum upto the given amount.

@author: Kelum Perera
twitter handle- @kelum0823

"""

import pandas as pd

df = pd.DataFrame(data={'value':[10850,20958,44999,1484.25,0.5,4.85],})


def my_denomination(amount):
    notes = [5000,1000, 500, 100, 50, 20, 10, 5,2,1,0.5,0.25]
    noteCounter = [0, 0, 0, 0, 0,0, 0, 0, 0, 0,0,0]
    j1 = []
    for i, j in zip(notes, noteCounter):
        if amount >= i:
                j = amount // i
                amount = amount - j * i
                #print (i ," : ", j)
        else:
            j= 0
        j = int(j)
        j1.append(j)
    return j1                
    

df[[ '5000','1000','500','100','50','20','10','5','2','1','0.50','0.25']] = df.apply(lambda row: pd.Series(my_denomination(row['value'])), axis=1)

