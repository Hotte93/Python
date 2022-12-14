
from tkinter import *
import tkinter as tk
import time
from pyModbusTCP.server import ModbusServer



server = ModbusServer("172.16.2.190",502, no_block=True)
server.start()
   
# Create a Window
root = tk.Tk()

root.geometry("300x290")
# Edit Title
root.title("Resolve Batterie Profil")




#Edit fields for Descrition
#------------------------------------------------------------------------------
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
    
#Edit fields for data entry
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
    
#
#------------------------------------------------------------------------------
      
def print_entry():
    #server= ModbusServer("172.16.2.190",502, no_block=True)
    
    print("\n")
    print("Server is run:" + str(server.is_run)) 
    
    print("Value before writing:" + str(server.data_bank.get_input_registers(7)))
    
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
        
    ConnectionFenster =Label(root,text = "connected", fg="black", bg="white")
    ConnectionFenster.place(y=200, x=90, width= 120, height= 30)
            

    server.data_bank.set_input_registers(7, [SOCEntry.get()])
    server.data_bank.set_input_registers(8, [SOHEntry.get()])
    server.data_bank.set_input_registers(9, [EntladeEntry.get()])
    server.data_bank.set_input_registers(10, [LadeEntry.get()])
    time.sleep(1)
               
    #except:
        #server.stop()
        #print("Server offline")
        

    print("Server is run:" + str(server.is_run)) 
    
    print("Value after writing:" + str(server.data_bank.get_input_registers(9)))
                  
   
 
#Button to entry print_entry()
#------------------------------------------------------------------------------
Button2= tk.Button(text="Write Data to Server",command= print_entry)
Button2.place(y=230, x=90,width= 120,height= 30)
    
#Button to close Programm
#------------------------------------------------------------------------------
QuitButton = tk.Button(text="Close Programm", command=root.destroy)    
QuitButton.place(y=260, x=90,width= 120,height= 30)

        
root.mainloop()
