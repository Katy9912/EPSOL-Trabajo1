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
import shutil

#Libreria para exportar png de grafica
from selenium.webdriver import Chrome, ChromeOptions
options=ChromeOptions()
options.add_argument('--headless')
web_driver=Chrome(executable_path='C:\\EPSOL_APP\\chromedriver.exe',options=options)


    
#Clase Para obtener toda la data
class Graphic_Data:
    def __init__(self):
        #Diccionaria para las etiquetas de las graficas
        self.name= dict(
            PF="%",
           #HRMA="%"+"F",
            #HRMB="%"+"F",
            #HRMC="%"+"F",
            V="V",
            I="A",
            FR="Hz",
            P="W",
            THDI="%",
            THDB="%",
            KF="%",
            DP="%",
            IMBV="%",
            IMBI="%",
            PST="% Voltaje",
            PLT="% Voltaje",
            #MAGI=
            ANGI="°",
            #MAGV=
            ANGV="°",
            HI="A",
            HV="V",
            HW="W",
            WH="WH",
            UH="VAH",
            QH="VARH",
            VARH="VARH"
        )

        self.months_dic= {

        
            "Enero" : '01',
            "Febrero" : '02',
            "Marzo" : '03',
            "Abril" : '04',
            "Mayo" : '05',
            "Junio" : '06',
            "Julio" : '07',
            "Agosto" : '08',
            "Septiembre" : '09',
            "Octubre" : '10',
            "Noviembre" : '11',
            "Diciembre" : '12'
        }
            
    def setPath(self, path):
        self.path = path

    def new_gra(self,data):
        
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
        
        
                  
                
        return dataas

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
    
    #Metodo que permite obtener la lista de todas las variables
    #Disponibles para graficar
    def optionsToGraph(self, dataframe):

        graph = []
        data = dataframe.copy()
        dataas=self.new_gra(data)
        
        dataas_list = dataas.columns.tolist()

        for c in dataas_list:
            new_list = dataas[c]
            new_list = list(new_list[~(new_list==0)])
            for element in new_list:
                graph.append(element)

        return graph

    #Metodo que regresa los meses disponibles para filtrar
    def getMonths(self,dataframe):
        data = dataframe.copy()
        index = data.index.tolist()
        months = list(set(pd.DatetimeIndex(index).month_name(locale='Spanish')))
        months.insert(0,'Todos')
        return months

    # Función para generar nombres de ejes graficas
    def etiqueta(self,llave):
        guardar=self.name.get(llave)
        return guardar

    #Funcion que realiza el filtrado de datos7
    def makeFilter(self,date,dataframe):
        index = []
        data = dataframe.copy()
        selected_month = self.months_dic.get(date)
        dates = data.index.tolist()
        for element in dates:
            element_month = element.strftime('%m')
            if element_month == selected_month:
                index.append(element)
        result = data.loc[index]
        return result

                     

    #Funcion generadora de graficas
    def plot(self, dataframe, key, label_title, month_used):
        from bokeh.plotting import figure, output_file, save
        from bokeh.models import Range1d, HoverTool, ColumnDataSource, BoxAnnotation, Toggle
        from bokeh.io import output_notebook, show
        from bokeh.palettes import Spectral4, Category20_20, Category20b_20
        from bokeh.io import export_png        

        data = dataframe.copy()
        dataas=self.new_gra(data)
        new_c=dataas[key]        #   
        new_c=list(new_c[~(new_c==0)])        #                       
        
        #Codigo que permite corregir el problema de colores para las categorias >20 variables
        colors=[]
        if len(new_c)>20:    
            for c in Category20_20:
                colors.append(c)
            for c in Category20b_20:
                colors.append(c)
        else:
           colors= Category20_20
           colors=colors
        
        new_d=pd.DataFrame()                 #
        new_d=data[new_c]     
        if new_d.isnull().values.any():                      #   
            final=new_d.fillna(value=0)
        else:
            final=new_d
        
                        #   
        #final=new_d.dropna()              #
        label= self.etiqueta(llave=key)
        tools = ["pan", "box_zoom", "wheel_zoom", "save", "zoom_in", "zoom_out", "crosshair", "reset"]
        bp = figure(plot_width=1240, plot_height=600, x_axis_type="datetime", x_axis_label="Tiempo (t)", y_axis_label= str(label), toolbar_location='right',
                    sizing_mode="fixed", title=label_title + " [" + month_used +"]", tools=tools)
        bp.title.text_font_style = 'bold'
        bp.title.align = 'center'
        bp.toolbar.autohide = True


        for column, color in zip(list(final), colors):
            
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
        plot_name = str(f'{key} -plot' + time.strftime("%d-%m-%Y-%H-%M-%S") + " [" + month_used +"]"".html")   

        output_file(plot_name, title=key, mode="cdn")
        save(bp)
        filen=str(self.path+key + time.strftime("%d-%m-%Y-%H-%M-%S") + " [" + month_used +"]" '.png')
        export_png(bp, filename=filen,webdriver=web_driver)
        
        return plot_name

    def plotVariable(self, dataframe, variables, month):
        from bokeh.plotting import figure, output_file, save
        from bokeh.models import Range1d, HoverTool, ColumnDataSource, BoxAnnotation, Toggle
        from bokeh.io import output_notebook, show
        from bokeh.palettes import Spectral4, Category20_20, Category20b_20
        from bokeh.io import export_png        
        
        var = variables
        data = dataframe.copy()
        new_d=pd.DataFrame()                 #
        new_d=data[var]
        
        #Codigo que permite corregir el problema de colores para las categorias >20 variables
        colors=[]
        if len(var)>20:    
            for c in Category20_20:
                colors.append(c)
            for c in Category20b_20:
                colors.append(c)
        else:
           colors= Category20_20
           colors=colors

        if new_d.isnull().values.any():                      #   
            final=new_d.fillna(value=0)
        else:
            final=new_d
        
        tools = ["pan", "box_zoom", "wheel_zoom", "save", "zoom_in", "zoom_out", "crosshair", "reset"]
        bp = figure(plot_width=1240, plot_height=600,x_axis_type="datetime", x_axis_label="Tiempo (t)", toolbar_location='right',
                    sizing_mode="fixed", title="Personalizado"" [" + month + "]" , tools=tools)
        bp.title.text_font_style = 'bold'
        bp.title.align = 'center'
        bp.toolbar.autohide = True


        for column, color in zip(list(final), colors):
            
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
        plot_name = str('CUSTOMIZED-plot' + time.strftime("%d-%m-%Y-%H-%M-%S") + " [" + month + "]" + ".html")   
        output_file(plot_name, title="customized", mode="cdn")
        save(bp)
        
        filen=str(self.path+'CUSTOMIZED-plot' + time.strftime("%d-%m-%Y-%H-%M-%S")+ " [" + month + "]" + ".png") 
        export_png(bp, filename=filen,webdriver=web_driver)
    
        return plot_name         

        


if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    Data = Graphic_Data()
    initial_dir = "../ErickXD"
    filenames = filedialog.askopenfilenames(title="Selecciona los Archivos",
                                            initialdir=initial_dir,
                                            filetypes=(("Archivo CSV", "*.csv"), ("Todos los archivos", "*.*")))
    
    #filedialog.mainloop()
        
    data = Data.merge(filenames)
    #key='HRMA'
    #name,new_columns= Data.plot(data,key)
    keys=['PF','THDI','THDV','KF','DP','PST','PLT','WH','UH','QH','VARH','FR','MAG','ANG','IMB','MX','MN','HRMA','HRMB','HRMC','I','V','P']
    for key in keys:
        name= Data.plot(data,key)
         