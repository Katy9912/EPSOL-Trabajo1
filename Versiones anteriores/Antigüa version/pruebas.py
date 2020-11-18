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

categorias=dict(PF=['PFT3','LDPFT3','PFTA','LDPFTA','PFTB','LDPFTB','PFTC','LDPFTC'], 
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
                EnerAp=['UH3_DEL','UH3_REC'],
                EnerR=['QH3_DEL','QH3_REC','QHA_DEL','QHA_REC','QHB_DEL','QHB_REC','QHC_DEL','QHC_REC','QH3_NET'],
                EnerRA=['VARH3_DEL_LG','VARH3_DEL_LD','VARH3_REC_LG','VARH3_REC_LD'])

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



def new_gra(data):

    keys=['PF','THDI','THDV','KF','DP','PST','PLT','WH','UH','QH','VARH','FR','MAG','ANG','IMB','MX','MN']
    pruebas=list(data.columns)
    dataas=pd.DataFrame()
    pruebas_c=[]
    for i in keys:    
        k=0    
        for j in pruebas:
            p=j.find(i)
            
            if p>=0:            
                pruebas_c.append(j)
                dataas[i] =np.zeros(len(pruebas))            
                pruebas[k]=str(0)
        
            k=k+1    
        if len(pruebas_c)>0:
            dataas[i][0:len(pruebas_c)]=pruebas_c
            pruebas_c=[]
            
    HRMA=[] 
    HRMB=[] 
    HRMC=[] 
    
    
    keys='HRM'
    k=0
    for j in pruebas:
        p=j.find(keys)
        
        if p>=0:
            
            p1=j.find('A')
            if p1>=0:
                HRMA.append(j)
                dataas[str(keys+'A')] =np.zeros(len(pruebas))
            else:
                p1=j.find('B')
                if p1>=0:
                    HRMB.append(j)
                    dataas[str(keys+'B')] =np.zeros(len(pruebas))
                else: 
                    p1=j.find('C')
                    if p1>=0:
                        HRMC.append(j)
                        dataas[str(keys+'C')] =np.zeros(len(pruebas))
                
            pruebas[k]=str(0)
    
        k=k+1    
    if len(HRMA)>0:
        dataas[str(keys+'A')][0:len(HRMA)]=HRMA
        HRMA=[] 
    if len(HRMB)>0:
        dataas[str(keys+'B')][0:len(HRMB)]=HRMB
        HRMB=[] 
    if len(HRMC)>0:
        dataas[str(keys+'C')][0:len(HRMC)]=HRMC
        HRMC=[] 
    
    keys=['I','V']
    pruebas_c=[]
    for i in keys:    
        k=0    
        for j in pruebas:
            p=j.find(i)
            
            if p>=0:            
                pruebas_c.append(j)
                dataas[i] =np.zeros(len(pruebas))            
                pruebas[k]=str(0)
        
            k=k+1    
        if len(pruebas_c)>0:
            dataas[i][0:len(pruebas_c)]=pruebas_c
            pruebas_c=[]
            
    dataas['P'] =np.zeros(len(pruebas))
    pruebas=list(filter(lambda x: x != str(0), pruebas))
    if len(pruebas)>0:
        
        dataas['P'][0:len(pruebas)]=pruebas
    else:
        del dataas['P']
    
    return dataas

     
def merge(filenames,band):

    LDPS = [None] * len(filenames)
    
  
    
    for num, file in enumerate(filenames):
        LDPS[num]= clean(file,band)       
        
    
    merge = reduce(lambda left, right: pd.merge(left, right, on='Datetime', how='outer'), LDPS)
    
    merge = merge.sort_values(by=['Datetime'])
    merge = merge.reset_index(drop=True)
    merge = merge.set_index('Datetime')       

    return merge
   
#filenames=['DATOSDEsktopAPP\LDP Export 2020-jun.-23_09-17-21_Recorder13.csv']
#data = merge(filenames,False)
    


def plot(dataframe, key):
        from bokeh.plotting import figure, output_file, save
        from bokeh.models import Range1d, HoverTool, ColumnDataSource, BoxAnnotation, Toggle
        from bokeh.io import output_notebook, show
        from bokeh.palettes import Spectral4, Category20_20
        from bokeh.io import export_png        

        data = dataframe.copy()      
        dataas=new_gra(data)
        new_c=dataas[key]                   #   
        new_c=list(new_c[~(new_c==0)])       #   
                                             #
        new_d=pd.DataFrame()                 #
        new_d=data[new_c]                    #   
        final=new_d.dropna()     
        
        #final = new_file.dropna()    
        #final = data.loc[categorias[key]].dropna()
        #final = data[categorias[key]].dropna()
        
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
        return plot_name

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
data = merge(filenames,True)    
#data = Data.merge(filenames,False)
#key='HRMA'
#name= plot(data,key)




#PARA GRAFICAR########################
            #   
######################################
            
            
            
            
                
            
            
            
            
#keys     =['PF','THDI']
#keys=['PF','THDI','THDV','KF','DP','PST','PLT','WH','UH','QH','VARH','FR','MAG','ANG','IMB','MX','MN']
#keys=['PF','THDI','THDV','KF','DP','PST','PLT','WH','UH','QH','VARH','FR','MAG','ANG','IMB']
keys=['PF','THDI','THDV','KF','DP','PST','PLT','WH','UH','QH','VARH','FR']
dataas=pd.DataFrame()
back=list(data.columns)
df=data.copy()


np.shape(df)[1]
for j in keys:
    if np.shape(df)[1] >0:
        prueba=df.columns.str.contains(str(j))
        prueba1=list(df.columns[prueba])
        if len(prueba1)>0:
            dataas[j] =np.zeros(len(back))                
            dataas.loc[0:len(prueba1)-1,j]=prueba1
            for i in prueba1:
                del df[i]
    else:
        break            

if np.shape(df)[1] >0:
    keys='MAG'
    
    
    prueba=df.columns.str.contains('MAG')
    prueba1=df.loc[:,prueba]
    
    hrma=list(prueba1.columns[prueba1.columns.str.contains('V')])
    
    if len(hrma)>0:
        dataas[str(keys+'V')] =np.zeros(len(back))
        dataas.loc[0:len(hrma)-1,str(keys+'V')]=hrma
        for i in hrma:
                del df[i]
    
    prueba=df.columns.str.contains('MAG')
    prueba1=df.loc[:,prueba]
    hrmb=list(prueba1.columns)            
    if len(hrmb)>0:
        dataas[str(keys+'I')] =np.zeros(len(back))
        dataas.loc[0:len(hrmb)-1,str(keys+'I')]=hrmb
        for i in hrmb:
                del df[i]

                
if np.shape(df)[1] >0:
    keys='ANG'
    
    
    prueba=df.columns.str.contains('ANG')
    prueba1=df.loc[:,prueba]
    
    hrma=list(prueba1.columns[prueba1.columns.str.contains('V')])
    
    if len(hrma)>0:
        dataas[str(keys+'V')] =np.zeros(len(back))
        dataas.loc[0:len(hrma)-1,str(keys+'V')]=hrma
        for i in hrma:
                del df[i]
    
    prueba=df.columns.str.contains('ANG')
    prueba1=df.loc[:,prueba]
    hrmb=list(prueba1.columns)            
    if len(hrmb)>0:
        dataas[str(keys+'I')] =np.zeros(len(back))
        dataas.loc[0:len(hrmb)-1,str(keys+'I')]=hrmb
        for i in hrmb:
                del df[i]

if np.shape(df)[1] >0:
    keys='IMB'
    
    
    prueba=df.columns.str.contains('IMB')
    prueba1=df.loc[:,prueba]
    
    hrma=list(prueba1.columns[prueba1.columns.str.contains('V')])
    
    if len(hrma)>0:
        dataas[str(keys+'V')] =np.zeros(len(back))
        dataas.loc[0:len(hrma)-1,str(keys+'V')]=hrma
        for i in hrma:
                del df[i]
    
    prueba=df.columns.str.contains('IMB')
    prueba1=df.loc[:,prueba]
    hrmb=list(prueba1.columns)            
    if len(hrmb)>0:
        dataas[str(keys+'I')] =np.zeros(len(back))
        dataas.loc[0:len(hrmb)-1,str(keys+'I')]=hrmb
        for i in hrmb:
                del df[i]
    
            
if np.shape(df)[1] >0:
    keys='HRM'
    
    
    prueba=df.columns.str.contains('HRM')
    prueba1=df.loc[:,prueba]
    
    hrma=list(prueba1.columns[prueba1.columns.str.contains('A')])
    hrmb=list(prueba1.columns[prueba1.columns.str.contains('B')])
    hrmc=list(prueba1.columns[prueba1.columns.str.contains('C')])
    
    if len(hrma)>0:
        dataas[str(keys+'A')] =np.zeros(len(back))
        dataas.loc[0:len(hrma)-1,str(keys+'A')]=hrma
        for i in hrma:
                del df[i]
                
    if len(hrmb)>0:
        dataas[str(keys+'B')] =np.zeros(len(back))
        dataas.loc[0:len(hrmb)-1,str(keys+'B')]=hrmb
        for i in hrmb:
                del df[i]
                
    if len(hrmc)>0:
        dataas[str(keys+'C')] =np.zeros(len(back))
        dataas.loc[0:len(hrmc)-1,str(keys+'C')]=hrmc
        for i in hrmc:
                del df[i]


if np.shape(df)[1] >0:
    
    
    minimos=df.columns.str.contains('MN')
    maximos=df.columns.str.contains('MX')
    prueba1=df.loc[:,minimos]
    prueba2=df.loc[:,maximos]
    prueba1=pd.concat([prueba1,prueba2],axis=1)
    #prueba3
    hrma=list(prueba1.columns[prueba1.columns.str.contains('I')])
    hrmb=list(prueba1.columns[prueba1.columns.str.contains('V')])
    hrmc=list(prueba1.columns[prueba1.columns.str.contains('3')])
    
    if len(hrma)>0:
        dataas['HI'] =np.zeros(len(back))
        dataas.loc[0:len(hrma)-1,'HI']=hrma
        for i in hrma:
                del df[i]
                
    if len(hrmb)>0:
        dataas['HV'] =np.zeros(len(back))
        dataas.loc[0:len(hrmb)-1,'HV']=hrmb
        for i in hrmb:
                del df[i]
                
    if len(hrmc)>0:
        dataas['HW'] =np.zeros(len(back))
        dataas.loc[0:len(hrmc)-1,'HW']=hrmc
        for i in hrmc:
                del df[i]



                
if np.shape(df)[1] >0:
    keys=['I','V']
    for j in keys:
        prueba=df.columns.str.contains(str(j))
        prueba1=list(df.columns[prueba])
        if len(prueba1)>0:
            dataas[j] =np.zeros(len(back))                
            dataas.loc[0:len(prueba1)-1,j]=prueba1
            for i in prueba1:
                del df[i]
if np.shape(df)[1] >0:
    back2=list(df.columns)
    if len(back2)>0:
        dataas['P'] =np.zeros(len(back))
        power=list(df.columns)
        dataas.loc[0:len(power)-1,'P']=power

