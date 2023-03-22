
from tkinter import * #Importar libreria
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk

#Ventana
raiz= Tk()
raiz.title("Convertidor")
raiz.geometry("400x500")

#Variables
NA=IntVar()




#Frame
frame=Frame(raiz,bg="#707070")
frame.pack(fill="both",expand=1)

def Convertir():
   
    
    if  Moneda1.get() == "Moneda1" and Moneda2.get() == "Moneda2":
        print(f'Escoge las monedas que desees convertir')
    elif Moneda1.get() == "Moneda1":
        print(f'Escoge la Moneda 1')
    elif Moneda2.get() == "Moneda2":
        print(f'Escoge la Moneda 2')
    
    
    elif Moneda1.get() == "PesosMXN" and Moneda2.get()== "Dolares":
        resultado=NA.get()*0.054
        print(f'{NAEntry.get()} {Moneda1.get()} es igual a: {resultado} {Moneda2.get()}')
        Reslabel.config(text=resultado)
    elif Moneda1.get() == "PesosMXN" and Moneda2.get()== "Yenes":
        resultado=NA.get()*7.12
        print(f'{NAEntry.get()} {Moneda1.get()} es igual a: {resultado} {Moneda2.get()}')
        Reslabel.config(text=resultado)
    
    elif Moneda1.get() == "Dolares" and Moneda2.get()== "PesosMXN":
        resultado=NA.get()*18.61
        print(f'{NAEntry.get()} {Moneda1.get()} es igual a: {resultado} {Moneda2.get()}')
        Reslabel.config(text=resultado)
    elif Moneda1.get() == "Dolares" and Moneda2.get()== "Yenes":
        resultado=NA.get()*132.53
        print(f'{NAEntry.get()} {Moneda1.get()} es igual a: {resultado} {Moneda2.get()}')
        Reslabel.config(text=resultado)
        
    elif Moneda1.get() == "Yenes" and Moneda2.get()== "PesosMXN":
        resultado=NA.get()*0.14
        print(f'{NAEntry.get()} {Moneda1.get()} es igual a: {resultado} {Moneda2.get()}')
        Reslabel.config(text=resultado)
    elif Moneda1.get() == "Yenes" and Moneda2.get()== "Dolares":
        resultado=NA.get()*0.0075
        print(f'{NAEntry.get()} {Moneda1.get()} es igual a: {resultado} {Moneda2.get()}')
        Reslabel.config(text=resultado)
        
        
    else:
        print(f'Escoge monedas diferentes')
        Reslabel.config(text="")


        


#Etiqueta Numero A
labelNA=Label(frame,text="Producto: ",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.2)
#Entry Numero A
NAEntry=Entry(frame,
                  font=("Roboto",15,"bold"),
                  textvariable=NA)
NAEntry.place(relx=0.4,rely=0.2)

#Etiqueta Resultado
labelRes=Label(frame,text="Resultado: ",
                     font=("Roboto",15,"bold"),
                     bg="#707070",
                     fg="#f7f7f7").place(relx=.1 ,rely=.7)
#Etiqueta Resultado
Reslabel=Label(frame,text=" ",
                     font=("Roboto",20,"bold"),
                     bg="#707070",
                     fg="#f7f7f7")
Reslabel.place(relx=.5 ,rely=.7)


#Selector Moneda 1
Moneda1 = ttk.Combobox(frame,state="readonly")
Moneda1.place(relx=.1,rely=.5)
Moneda1["values"]=("Moneda1","PesosMXN","Dolares","Yenes")
Moneda1.current(0)


#Selector Moneda2
Moneda2 = ttk.Combobox(frame,state="readonly")
Moneda2.place(relx=.55,rely=.5)
Moneda2["values"]=("Moneda2","PesosMXN","Dolares","Yenes")
Moneda2.current(0)



#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                         B O T O N E S 


#Boton
boton=Button(frame,text="Convertir",
             font=("Roboto",20,"bold"),
             width=15,
             height=1,
             command=Convertir).place(relx=.15,rely=.85)




raiz.mainloop()


