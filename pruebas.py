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
import os, time

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
   
#filenames=['DATOSDEsktopAPP\LDP Export 2020-jun.-23_09-17-21_Recorder13.csv']
#data = merge(filenames,False)
    

def grupos(data,key,col):
    
    g=[]
    for pos in col:
         para_b=data.iloc[:,pos]
         para_b=para_b.dropna()
         ind=len(para_b)-1
         para_b.loc[para_b.index[ind]]=None
         para_b=len(para_b.dropna())
         g.append(para_b)
    g2=np.sum(g)
    #del merge[merge.columns[min(col)]]         
    m=max(np.where(data.values==key)[1])
    f=m-(g2+1)
    new_columns=list(data.columns[f:m])
    
    del data[new_columns[g[1]]]
    new_columns=list(data.columns[f:m-1])
    return new_columns


def plot(dataframe, key):
        from bokeh.plotting import figure, output_file, save
        from bokeh.models import Range1d, HoverTool, ColumnDataSource, BoxAnnotation, Toggle
        from bokeh.io import output_notebook, show
        from bokeh.palettes import Spectral4, Category20_20
        from bokeh.io import export_png        

        data = dataframe.copy()      
        new_columns=list()
        
        col=len(np.where(data.columns==str(key))[0])
        
        if col == 0:
            
            col=np.where(data.values==str(key))[1]
            new_columns=grupos(data,key,col)            
        
        else:
            col=int(np.where(data.columns==str(key))[0])
            para_b=data.iloc[:,col]    
            para_b=para_b.dropna()
            ind=len(para_b)-1
            para_b.loc[para_b.index[ind]]=None
            para_b=len(para_b.dropna())        
            columnas=col-para_b
            new_columns=list(data.columns[columnas:col])
        
        new_file=pd.DataFrame()
        
        for i in new_columns:
            c=data[i]
            new_file[i]=c
        
        final = new_file.dropna()        
        
        tools = ["pan", "box_zoom", "wheel_zoom", "save", "zoom_in", "zoom_out", "crosshair", "reset"]
        bp = figure(width=500, height=300, x_axis_type="datetime", toolbar_location='right',
                    sizing_mode="scale_width", title=key, tools=tools)
        bp.toolbar.autohide = True


        for column, color in zip(list(final), Category20_20):
            
            cds = ColumnDataSource(final)
            a = bp.circle(x='Datetime', y=column, source=cds, fill_alpha=0.0, line_alpha=0.0, size=5)
            bp.step(x='Datetime', y=column, source=cds, mode="after", line_color=color, legend_label=column)
            hover = HoverTool(
                tooltips=[
                    ("Datetime", "@Datetime{%Y-%m-%d %H:%M:%S}"), (column, f"@{column}")
                        ],
                formatters={"@Datetime": "datetime"}, mode='vline', renderers=[a], toggleable=False)

            bp.add_tools(hover)

        bp.legend.location = "top_left"
        bp.legend.click_policy = "hide"
        plot_name = str(f'{key} -plot' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".html")   

        output_file(plot_name, title=key, mode="cdn")
        save(bp)
        #se demora mucho cuando va a exportar
        #filen=str('./Imagenes/'+key+'.png')
        #export_png(bp, filename=filen, height=6, width=8)
        return plot_name,new_columns

#for key in Data.mediciones_dict:
#    name= Data.plot(data,key)

import tkinter as tk
from tkinter import filedialog

initial_dir = "../ErickXD" 
#filenames=['\LDP Export 2020-jun.-23_09-17-21_Recorder13.csv']
filenames = filedialog.askopenfilenames(title="Selecciona los Archivos",
                                            initialdir=initial_dir,
                                            filetypes=(("Archivo CSV", "*.csv"), ("Todos los archivos", "*.*")))
    
filedialog.mainloop()
data = merge(filenames,False)    
#data = Data.merge(filenames,False)
key='HRMA'
name,new_columns= plot(data,key)