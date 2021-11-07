# -*- coding: utf-8 -*-
import pandas as pd
import random

df = pd.read_excel(r'')
'print(df.to_string())'

row = 0

while (1):
    
    cellFName = df.iloc[row,0]
    cellLName = df.iloc[row,1]
    
    if cellFName == 'END':
        break
    
    'Password Generator---------------------------------------------------------'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    symbol = '!@#$%^&*()_+'
    
    combinePass = lower+upper+num+symbol
    length = 10
    password = "".join(random.sample(combinePass,length))
    print (password)
    df.iloc[row,3] = password
    
    'Email Generator-------------------------------------------------------------'
    email = cellFName+cellLName+"".join(random.sample(num,5))
    print (email)
    df.iloc[row,2] = email
    
    'Place Email into Excel------------------------------------------------------'
    writer = pd.ExcelWriter('UsernamePass.xlsx')
    df.to_excel(writer,'new_sheet')
    writer.save()
    row = row + 1
