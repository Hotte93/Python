# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:56:26 2022

Aktuell:
    Funktion kann per Knopfdruck in Register schreiben.
    Über erneuten Aufruf von after() wird die funktion mit einem bestimmten
    Intervall erneut aufgerufen
    Es muss noch Lifesign Register hinzugefügt werden
    




@author: JHOSSBACH
"""
from tkinter import *
import tkinter as tk
import time
from pyModbusTCP.server import ModbusServer, DataBank



   
# Ein Fenster erstellen
root = tk.Tk()
#Größe des Fensters einstellen
root.geometry("300x290")
# Den Fenstertitle erstellen
root.title("Resolve Batterie Profil")


#Erstellen einer Variable vom Typ Int
text_variable = tk.IntVar()
#Wert der erstellten Variable festlegen
text_variable.set(6000)


#Konstruktor für den ersten Container, in diesem können weiter Container/Fenster angezeigt werden
#IPFensterFrame=Frame(root, bg="white",)  # Set the background color
#IPFensterFrame.place(y=0, x=0, width= 250,height= 30)

IPFensterLabel=Label(root,  text="Server IP", fg="black", bg= "white")
IPFensterLabel.place(y=0, x=0, width= 100,height= 30)

PortFenster =Label(root,text = "Port", fg="black", bg="white")
PortFenster.place(y=30, x=0, width= 100, height= 30)

SOCFenster =Label(root,text = "SOC", fg="black", bg="white")
SOCFenster.place(y=80, x=0, width= 100, height= 30)

SOHFenster =Label(root,text = "SOH", fg="black", bg="white")
SOHFenster.place(y=110, x=0, width= 100, height= 30)

EntladeFenster =Label(root,text = "Entladeleistung", fg="black", bg="white")
EntladeFenster.place(y=140, x=0, width= 100, height= 30)

LadeFenster =Label(root,text = "Ladeleistung", fg="black", bg="white")
LadeFenster.place(y=170, x=0, width= 100, height= 30)

#Anlegen der Felder für die Eingabe der Werte
#------------------------------------------------------------------------------
IPEntry=Entry(root,fg="black", bg="white")
IPEntry.place(y=0, x=100,width= 100,height= 30)

PortEntry=Entry(root,fg="black", bg="white")
PortEntry.place(y=30, x=100,width= 100,height= 30)

SOCEntry=Entry(root,fg="black", bg="white")
SOCEntry.place(y=80, x=100,width= 100,height= 30)

SOHEntry=Entry(root,fg="black", bg="white")
SOHEntry.place(y=110, x=100,width= 100,height= 30)

EntladeEntry=Entry(root,fg="black", bg="white")
EntladeEntry.place(y=140, x=100,width= 100,height= 30)

LadeEntry=Entry(root,fg="black", bg="white")
LadeEntry.place(y=170, x=100,width= 100,height= 30)

#Wird aufgerufen um den eingegebenen Text auszugeben
#------------------------------------------------------------------------------
def print_entry():

    IPFensterLabel=Label(root,  text=IPEntry.get(), fg="black", bg= "white")
    IPFensterLabel.place(y=0, x=200, width= 100,height= 30)

    PortFenster =Label(root,text = PortEntry.get(), fg="black", bg="white")
    PortFenster.place(y=30, x=200, width= 100, height= 30)

    SOCFenster =Label(root,text = SOCEntry.get(), fg="black", bg="white")
    SOCFenster.place(y=80, x=200, width= 100, height= 30)

    SOHFenster =Label(root,text = SOHEntry.get(), fg="black", bg="white")
    SOHFenster.place(y=110, x=200, width= 100, height= 30)

    EntladeFenster =Label(root,text = EntladeEntry.get(), fg="black", bg="white")
    EntladeFenster.place(y=140, x=200, width= 100, height= 30)

    LadeFenster =Label(root,text = LadeEntry.get(), fg="black", bg="white")
    LadeFenster.place(y=170, x=200, width= 100, height= 30)

    ConnectionFenster =Label(root,text = "verbunden", fg="black", bg="white")
    ConnectionFenster.place(y=200, x=90, width= 120, height= 30)
    
    

    #server = ModbusServer(IPEntry.get(), int(PortEntry.get()), no_block=True)
    server = ModbusServer("172.16.254.133", 502, no_block=True)
    
    
    try:
        
        server.start()
       
        #print("Ging")
            
        #Data = {168:40001, 2:40002, 3:40003, 4:40004, 5:40005, 6:40006}
           
        #print("test")
        #print(server.is_run)
         
            
            
        server.data_bank.set_input_registers(168, [SOCEntry.get()])
        server.data_bank.set_input_registers(169, [SOHEntry.get()])
        server.data_bank.set_input_registers(171, [EntladeEntry.get()])
        server.data_bank.set_input_registers(172, [LadeEntry.get()])
        server.data_bank.set_input_registers(174, ['34'])
        
                
    #print("test1")
        #server.data_bank.set_holding_registers(2, [250])
        #server.data_bank.set_holding_registers(1, 130)
        #server.data_bank.set_holding_registers(3, int(450))
        #exit()
        #DataBank.set_words(2, int(3500));
        #server.stop()
            
        #QuitButton = tk.Button(text="Programm beenden", command=root.destroy)    
        #QuitButton.place(y=260, x=90,width= 120,height= 30)
            
        #Button2= tk.Button(text="Eingabe ausgeben",command= print_entry)
        #Button2.place(y=230, x=90,width= 120,height= 30)
        
        
        
        
        
    except:
       
        print("Ging nicht")
        
    root.after(100, print_entry)
 

        

    
    
    


#Button übergibt die Einträge aus der UI an das Programm
#------------------------------------------------------------------------------
Button2= tk.Button(text="Eingabe ausgeben",command= print_entry)
Button2.place(y=230, x=90,width= 120,height= 30)

#Button beendet bei Klicken das Programm
#------------------------------------------------------------------------------
QuitButton = tk.Button(text="Programm beenden", command=root.destroy)    
QuitButton.place(y=260, x=90,width= 120,height= 30)


#print(server.data_bank.get_input_registers(168))



'''
fill="x"                Button über die gesamte X-Achse
fill="y"                Button über die gesamte Y-Achse
padding=10              Abstand des Buttons von oberer Kante
command= sayhello       Funktion übergeben die dann auf der Console ausgegeben wird
command= root.destroy   Fenster wird geschlossen
state= tk.DISABLE       Button kann deaktiviert werden, also nicht mehr klickbar
state= tk.NORMAL        Button kann aktiviert werden, ist default auf NORMAL


for item in PortFenster.place():          #Funktion zeigt die möglichen Einträge für das Objekt 
  print(item, ":", Button[item])


#------------------------------------------------------------------------------

entry = tk.Entry(root, fg="yellow", bg="blue", width=50)

entry.pack()

#------------------------------------------------------------------------------


# In der Ereignisschleife auf Eingabe des Benutzers warten.

'''


    
root.mainloop()