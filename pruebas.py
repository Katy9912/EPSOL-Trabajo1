# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:14:12 2020

@author: nboni
"""



import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from functools import reduce
import csv

def clean(path,band):

        palabra = "Record"   
     
        with open(path, newline='') as File:
            reader = csv.reader(File)
            for index, row in enumerate(reader):
        
                if row[0] == palabra:
                    cut_index = index        
        
        try:                   
            data = pd.read_csv(path, skiprows=cut_index, delimiter='""'and',', engine='python')    
        except Exception as e:   
            data = pd.read_csv(path, skiprows=cut_index, delimiter=', ', engine='python')       
            print(e)
            
        data.columns = data.columns.str.replace('"', "")
        data.columns = data.columns.str.replace(' ', "")
        data['Date'] = data['Date'].map(str) + "." + data['Time'].map(str)
        try:
            data['Date'] = pd.to_datetime(data['Date'], infer_datetime_format=True)                
        except Exception as e: 
               
               data=data.dropna(axis=0)
               data['Date'] = pd.to_datetime(data['Date'], infer_datetime_format=True)
               
        data = data.rename(columns={'Date': 'Datetime'})                    
        
        del data['Time']
        del data['Status']
        del data['Record']
        if band == True:
            data=data.loc[:, ~data.columns.str.contains('^Unnamed')]    
            return data.copy()
        elif band== False:
            dat=data.dropna(axis=1)
            dat=dat.loc[:, ~dat.columns.str.contains('^Unnamed')]    
            
            name=None            
            new =[None]*(len(dat))            
            palabra=dat.columns[1]            
            columns=list(dat.columns[1:np.shape(dat)[1]])
            new[0:len(columns)]=columns                    
            index=palabra.find('_')
            if index > 0:
               if palabra[0].isdigit():               
                   name=palabra[-3:len(palabra)]
                   new[len(columns)]=name
               else:
                   name=str(palabra[0:3]+palabra[-1])
                   new[len(columns)]=name         
                
            else:             
                if len(palabra) > 2:                
                    name=palabra[0:2]
                    new[len(columns)]=name      
                else:
                    name=palabra[0:1]     
                    new[len(columns)]=name
            dat[name]=new                  
                
            return dat.copy()
        
        

   
        
def merge(filenames,band):

    LDPS = [None] * len(filenames)
  
    
    for num, file in enumerate(filenames):
        LDPS[num] = clean(file,band)       
        
    
    merge = reduce(lambda left, right: pd.merge(left, right, on='Datetime', how='outer'), LDPS)
    
    merge = merge.sort_values(by=['Datetime'])
    merge = merge.reset_index(drop=True)
    merge = merge.set_index('Datetime')       

    return merge
   
filenames=['DATOSDEsktopAPP\LDP Export 2020-jun.-23_09-17-21_Recorder13.csv']
data = merge(filenames,False)

#for key in Data.mediciones_dict:
#    name= Data.plot(data,key)