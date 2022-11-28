# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:45:55 2022

@author: JHOSSBACH
"""

from pyModbusTCP.server import ModbusServer

while(True):
    server = ModbusServer("", 502, no_block=True)

    try:
    
        
        server.start()
    
    except:
        print("Ging nicht")

  
    Data = {1:300, 2:350}

    server.data_bank.set_holding_registers(2, [250])
    server.data_bank.set_holding_registers(1, [130])
    server.data_bank.set_holding_registers(3, [int(450)])

    #DataBank.set_words(2, int(3500));
    #server.stop()