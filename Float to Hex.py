# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:34:40 2022

@author: JHOSSBACH
"""

import struct
import binascii

#FUNKTION
###############################################################################
while(True):
    
   
    print("Auswahl treffen: ")
    
    print("1   int to hex/dec (HyCon)")
    print("2   float32 to hex/dec")
    print("3   hex to float")
    


    auswahl= input()


#Int to hex/dec    
#------------------------------------------------------------------------------
    if(auswahl=='1'):
        
        print("\n")
        y= input("Zahl eingeben:")
        y1=int(y) #Variable zu Integeer wandeln
        print("\n")
        print("----------------------")
        
        print("Oberes  Register",binascii.hexlify((struct.pack(">i", y1)))[0:4].upper()) #Wert wird zunächst in Binärformat gepackt, dann in Hex-Wert gewandelt
        print("Unteres Register",binascii.hexlify((struct.pack(">i", y1)))[4:8].upper())
        x= binascii.hexlify((struct.pack(">i", y1)))[0:4]
        x1= binascii.hexlify((struct.pack(">i", y1)))[4:8]
        print("\n")
        print("Oberes  Register",int(x, 16))
        print("Unteres Register",int(x1, 16))
        print("----------------------")
        print("\n")
#------------------------------------------------------------------------------    




#Float to hex/dec    
#------------------------------------------------------------------------------    
 
    if(auswahl=='2'):
        print("\n")
        y= input("Zahl eingeben:")
        y1=float(y)
        
        print(binascii.hexlify((struct.pack(">f", y1)))[0:4].upper())
        print(binascii.hexlify((struct.pack(">f", y1)))[4:8].upper())
        x= binascii.hexlify((struct.pack(">f", y1)))[0:4]
        x1= binascii.hexlify((struct.pack(">f", y1)))[4:8]
        
        print(int(x, 16))
        print(int(x1, 16))
        print("\n\n")
        
        
#hex to float        
#------------------------------------------------------------------------------          
    if(auswahl=='3'):
            
        print("\n")
        print("HexWert eingeben:" )
        y2=input()
        print("\n")
        x3= struct.unpack('>f', bytes.fromhex(y2))[0]
        print(round(x3, 3))
    
#------------------------------------------------------------------------------  


###############################################################################


