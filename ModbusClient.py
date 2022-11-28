# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:10:23 2022

@author: JHOSSBACH
"""

from pyModbusTCP.client import ModbusClient
import time

client = ModbusClient('172.16.254.133', port=505)
y= client.open()
x =client.read_input_registers(0,125)
print(x)
time.sleep(0.5)
client.close()
