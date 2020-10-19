# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:11:46 2020

@author: nboni
"""


import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from functools import reduce
import csv


import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from functools import reduce
import csv

def __clean(path):
    
    palabra = "Record"
    
    path='DATOSDEsktopAPP\LDP Export 2020-jun.-23_09-17-21_Recorder11.csv'
    #path=r'C:\Users\nboni\OneDrive\Documents\GitHub\EPSOL-Trabajo1\Scripts\LDP Export 2020-may.-22_01-00-24_Recorder2.csv'
 
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
        
    

         
                         
        
    
    #Funcoion que hace el merge de los dataframes
def merge(filenames,band):
    
    LDPS = [None] * len(filenames)
      
    
    for num, file in enumerate(filenames):
        if band == False:
            LDPS[num] =__clean(file)       
        else: print('no')
    
    merge = reduce(lambda left, right: pd.merge(left, right, on='Datetime', how='outer'), LDPS)
    
    merge = merge.sort_values(by=['Datetime'])
    merge = merge.reset_index(drop=True)
    merge = merge.set_index('Datetime')      
    
    return merge
    


initial_dir = "../ErickXD"
filenames = filedialog.askopenfilenames(title="Selecciona los Archivos",
                                        initialdir=initial_dir,
                                        filetypes=(("Archivo CSV", "*.csv"), ("Todos los archivos", "*.*")))

filedialog.mainloop()
    
#data= merge(filenames,False)




p=[]
for f in filenames:
    pp=__clean(f)  
    p.append(pp)