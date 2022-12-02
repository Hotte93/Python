# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:45:55 2022

@author: JHOSSBACH
"""

from pyModbusTCP.server import ModbusServer
from pyModbusTCP.client import ModbusClient


client = ModbusClient('192.168.0.252', port=502)
y= client.open()
#x =client.read_input_registers(0,125)
client.write_single_register(90, 200)
while(True):
    server = ModbusServer("192.168.0.252", 502, no_block=True)

    try:
    
        
        server.start()
    
    except:
        print("Ging nicht")


  
    Data = {1:300, 2:350}

    server.data_bank.set_input_registers(2, [250])
    server.data_bank.set_input_registers(1, [130])
    server.data_bank.set_input_registers(3, [int(450)])

    #DataBank.set_words(2, int(3500));
    #server.stop()