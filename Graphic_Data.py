# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:13:55 2020

@author: nboni
"""

import os, time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from functools import reduce
import csv
from selenium.webdriver import Chrome, ChromeOptions
options=ChromeOptions()
options.add_argument('--headless')
web_driver=Chrome(executable_path='chromedriver_win32\chromedriver.exe',options=options)
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
        
    
#Clase Para obtener toda la data
class Graphic_Data:
    def __init__(self):
        #Declaración de un diccionario para agrupar graficas por tema o categoria
        self.mediciones_dict = dict(
           
            PF=['PFT3','LDPFT3','PFTA','LDPFTA','PFTB','LDPFTB','PFTC','LDPFTC'], 
                HRMA=['HRM3_IA','HRM5_IA','HRM7_IA','HRM9_IA','HRM11_IA','HRM13_IA','HRM15_IA','HRM17_IA',
                          'HRM19_IA','HRM21_IA','HRM23_IA','HRM25_IA','HRM27_IA','HRM29_IA','HRM31_IA','HRM33_IA',
                          'HRM35_IA','HRM37_IA','HRM39_IA','HRM41_IA','HRM43_IA','HRM45_IA','HRM47_IA','HRM49_IA'],
                HRMB=['HRM25_IB','HRM3_IB','HRM27_IB','HRM5_IB','HRM7_IB','HRM9_IB','HRM11_IB','HRM13_IB','HRM15_IB',
                      'HRM17_IB','HRM19_IB','HRM21_IB','HRM23_IB','HRM29_IB','HRM31_IB','HRM33_IB','HRM35_IB',
                      'HRM37_IB','HRM39_IB','HRM41_IB','HRM43_IB','HRM45_IB','HRM47_IB','HRM49_IB'],
                HRMC=['HRM3_IC','HRM5_IC','HRM7_IC','HRM23_IC','HRM9_IC','HRM11_IC','HRM13_IC','HRM15_IC','HRM17_IC',
                      'HRM19_IC','HRM21_IC','HRM25_IC','HRM27_IC','HRM29_IC','HRM31_IC','HRM33_IC','HRM35_IC','HRM37_IC',
                      'HRM39_IC','HRM41_IC','HRM43_IC','HRM45_IC','HRM47_IC','HRM49_IC'],
                Voltaje=['VA','VB','VC','VAB','VBC','VCA','V_AVE'],
                Corriente=['IA','IB','IC','I_AVE'],
                Frecuencia=['FREQ'],
                Potencia=['W3','U3','Q3','QA','QB','QC','UA','UB','UC','WA','WB','WC'], 
                DistorsionI=['THDIA','THDIB','THDIC','THDIN'],
                DistorsionV=['THDVA','THDVB','THDVC'],
                FactorK=['KFA','KFB','KFC'],
                FactorDP=['DPA','DPB','DPC','DP3'],
                DesbalanceI=['I0_IMB'],
                DesbalanceV=['V0_IMB','V_IMB','I_IMB'],
                FlickerPST=['PST_10MIN_VA','PST_10MIN_VB','PST_10MIN_VC'],
                FlickerPLT=['PLT_VA','PLT_VB','PLT_VC'],
                MagI=['3I0_MAG','I1_MAG','3I2_MAG'],
                AngI=['I1_ANG','3I0_ANG','3I2_ANG'],
                MagV=['3V0_MAG','V1_MAG','V2_MAG'],
                AngV=['3V0_ANG','V1_ANG','V2_ANG'],
                HistoI=['IAMX','IAMN','IBMX','IBMN','ICMX','ICMN','INMX','INMN'],
                HistoV=['VAMX','VAMN','VBMX','VBMN','VCMX','VCMN'],
                HistoP=['W3MX','W3MN','U3MX','U3MN','Q3MX','Q3MN'],
                EnerAc=['WH3_DEL','WH3_REC','WHA_NET','WHB_NET','WH3_NET','WHC_NET'],
                EnerAp=['UH3_DEL','UH3_REC'],EnerR=['QH3_DEL','QH3_REC','QHA_DEL','QHA_REC','QHB_DEL','QHB_REC','QHC_DEL','QHC_REC','QH3_NET'],
                EnerRA=['VARH3_DEL_LG','VARH3_DEL_LD','VARH3_REC_LG','VARH3_REC_LD'])


    #Función que limpia los cvs
    def clean(self, path):
        

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
    
        data=data.loc[:, ~data.columns.str.contains('^Unnamed')]    
        return data.copy()
       
        
    def merge(self, filenames):

        LDPS = [None] * len(filenames)
  
    
        for num, file in enumerate(filenames):
            LDPS[num] =self.clean(file)       
            
        
        merge = reduce(lambda left, right: pd.merge(left, right, on='Datetime', how='outer'), LDPS)
        
        merge = merge.sort_values(by=['Datetime'])
        merge = merge.reset_index(drop=True)
        merge = merge.set_index('Datetime')       
        
        return merge
    
    

    #Funcion generadora de graficas
    def plot(self, dataframe, key):
        from bokeh.plotting import figure, output_file, save
        from bokeh.models import Range1d, HoverTool, ColumnDataSource, BoxAnnotation, Toggle
        from bokeh.io import output_notebook, show
        from bokeh.palettes import Spectral4, Category20_20
        from bokeh.io import export_png        

        data = dataframe.copy()      
        final = data[self.mediciones_dict[key]].dropna()  
        
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
        filen=str('./Imagenes/'+key+'.png')
        export_png(bp, filename=filen, height=6, width=8,webdriver=web_driver)
        return plot_name


if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    Data = Graphic_Data()
    initial_dir = "../ErickXD"
    filenames = filedialog.askopenfilenames(title="Selecciona los Archivos",
                                            initialdir=initial_dir,
                                            filetypes=(("Archivo CSV", "*.csv"), ("Todos los archivos", "*.*")))
    
    filedialog.mainloop()
        
    data = Data.merge(filenames)
    #key='HRMA'
    #name,new_columns= Data.plot(data,key)
    for key in Data.mediciones_dict:
        name= Data.plot(data,key)
         