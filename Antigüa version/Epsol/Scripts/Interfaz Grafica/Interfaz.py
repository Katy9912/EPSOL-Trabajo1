
from tkinter import *
from PIL import Image, ImageTk
import time

root_title = "EPSOL Soluciones en Sistemas de Potencia y Energía SA de CV"
root_width = 700
root_height = 500
x_initial = 300
y_initial = 60

root = Tk()
root.title(root_title)
root.resizable(True,True)
root.geometry(f'{root_width}x{root_height}+{x_initial}+{y_initial}')
root.iconbitmap("LogoEpsol.ico")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

#Frame Container
principal_frame = Frame(root)
principal_frame.pack()


#Labels
title_label = StringVar(value="Aplicacion para limpiar datos de los Load Profile del equipo\nSEL-735")
program_title = Label(principal_frame,textvariable=title_label,font=("Times","16"))
program_title.pack(pady=10)

note_string = StringVar(value="Nota: Solo son aceptados los datos\ndel Equipo SEL735 y exportados\ndesde "
                              "QuickSet en formato .CSV")
note_label = Label(principal_frame,textvariable=note_string,font=("Times","10"))
note_label.pack(side=RIGHT,after=program_title)

logo = Image.open("LogoEpsolCMYK.png").resize((200,100))
logo_photo = ImageTk.PhotoImage(logo)
logo_label = Label(principal_frame,image=logo_photo)
logo_label.pack(after=note_label,side=LEFT)

#Buttons
buttons_width= 30
buttons_height=3
container_frame= Frame(principal_frame)
container_frame.pack(after=program_title,pady=10)

load_file_button = Button(container_frame,text="Cargar Archivos",width=buttons_width,height=buttons_height)
load_file_button.pack(pady=10)

download_file_button = Button(container_frame,text="Descargar Archivos",width=buttons_width,height=buttons_height)
download_file_button.pack(pady=10)

graphic_button = Button(container_frame,text="Graficar",width=buttons_width,height=buttons_height)
graphic_button.pack(pady=10)

report_button = Button(container_frame,text="Generar Reporte",width=buttons_width,height=buttons_height)
report_button.pack(pady=10)


root.mainloop()
