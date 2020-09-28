import os, time
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from functools import reduce
import csv

#Clase Para obtener toda la data
class Graphic_Data:
    def __init__(self):
        #Declaración de un diccionario para agrupar graficas por tema o categoria
        self.mediciones_dict = dict(
            PFT3=['PFT3', 'PFTA', 'PFTB', 'PFTC', 'LDPFT3'],
            HRM3_IA=['HRM3_IA', 'HRM5_IA', 'HRM7_IA', 'HRM9_IA', 'HRM11_IA', 'HRM13_IA', 'HRM15_IA', 'HRM17_IA',
                  'HRM19_IA', 'HRM21_IA', 'HRM23_IA', 'HRM25_IA', 'HRM27_IA', 'HRM29_IA', 'HRM31_IA', 'HRM33_IA'])

    #Función que limpia los cvs
    def __clean(self, path):

        palabra = "Record"
        inde=[]
        rows=[]
        
        with open(path, newline='') as File:
            reader = csv.reader(File)
            for index, row in enumerate(reader):
                inde.append(index)
                rows.append(row)
                if row[0] == palabra:
                    cut_index = index
        
        new =[None]*(len(inde)-cut_index-1)
        new[0:len(rows[4])]=rows[4]    
        
        
        data = pd.read_csv(path, skiprows=cut_index, delimiter=', ', engine='python')
        data.columns = data.columns.str.replace('"', "")
        data['Date'] = data['Date'].map(str) + "." + data['Time'].map(str)
        data['Date'] = pd.to_datetime(data['Date'], format="%m/%d/%Y.%H:%M:%S")
        data = data.rename(columns={'Date': 'Datetime'})
        data['Tipo']=new
        
        del data['Time']
        del data['Status']
        del data['Record']
        
        return data.copy()

    #Funcoion que hace el merge de los dataframes
    def merge(self, filenames):

        LDPS = [None] * len(filenames)
        #print(LDPS)
        for num, file in enumerate(filenames):
            LDPS[num] = self.__clean(file)
            

        #merge = reduce(lambda left, right: pd.merge(left, right, on='Datetime', how='outer'), LDPS)
        
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
        #col=int(np.where(data.values==str(key))[1])
        
        col=int(np.where(data.values==str(key))[1])
        para_b=data.iloc[:,col]       
        
        para_b=len(para_b.dropna())
        
        columnas=col-para_b
        new_columns=list(data.columns[columnas:col])
        
        new_file=pd.DataFrame()
        
        for i in new_columns:
            c=data[i]
            new_file[i]=c
        
        final = new_file['2020-04-01 00:00:00':'2020-04-02 00:00:00'].dropna()
        
        tools = ["pan", "box_zoom", "wheel_zoom", "save", "zoom_in", "zoom_out", "crosshair", "reset"]
        bp = figure(width=500, height=300, x_axis_type="datetime", toolbar_location='right',
                    sizing_mode="scale_width", title=key, tools=tools)
        bp.toolbar.autohide = True
        # green_box = BoxAnnotation(top=1, bottom=0.95, fill_color='blue', fill_alpha=0.1)
        # bp.add_layout(green_box)

        for column, color in zip(list(final), Category20_20):
            
            cds = ColumnDataSource(final)
            a = bp.circle(x='Datetime', y=column, source=cds, fill_alpha=0.0, line_alpha=0.0, size=5)
            bp.step(x='Datetime', y=column, source=cds, mode="after", line_color=color, legend=column)
            hover = HoverTool(
                tooltips=[
                    ("Datetime", "@Datetime{%Y-%m-%d %H:%M:%S}"), (column, f"@{column}")
                        ],
                formatters={"@Datetime": "datetime"}, mode='vline', renderers=[a], toggleable=False)

            bp.add_tools(hover)

        bp.legend.location = "top_left"
        bp.legend.click_policy = "hide"
        plot_name = str(f'{key} -plot' + time.strftime("%d-%m-%Y-%H-%M-%S") + ".html")
        #plot_name = str("mio.html")

        output_file(plot_name, title=key, mode="cdn")
        save(bp)
        #export_png(bp, filename=str(key))
        return plot_name,new_file


if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    Data = Graphic_Data()
    initial_dir = "../ErickXD"
    filenames = filedialog.askopenfilenames(title="Selecciona los Archivos",
                                            initialdir=initial_dir,
                                            filetypes=(("Archivo CSV", "*.csv"), ("Todos los archivos", "*.*")))
    
    filedialog.mainloop()
    
    
    merge = Data.merge(filenames)
    info=input()
    name= Data.plot(merge,info)
    
    #for key in Data.mediciones_dict:
    #    name,file= Data.plot(merge,key)

        

    #PFT3
    #HRM25_IB

