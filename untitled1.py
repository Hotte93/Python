# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:55:08 2022

@author: jens
"""
from pyModbusTCP.server import ModbusServer, DataBank
from random import uniform
import time

server= ModbusServer("192.168.0.252", 502, no_block=True)

try:
    print("Start Server")
    server.start()
    print("Serverist online")
    
    while True:
        server.data_bank.set_input_registers(3, [500])
        server.data_bank.set_input_registers(4, [600])
        server.data_bank.set_input_registers(5, [600])
        time.sleep(0.5)
except:
    print("Shutdown Server")
    server.stop()
    print("Server ist offline")
    