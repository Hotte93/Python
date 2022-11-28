# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:20:24 2022

@author: JHOSSBACH
"""

from pyModbusTCP.server import ModbusServer

server = ModbusServer("127.0.0.1", 12345, no_block=True)

x = server.start()

print(x)

Data = {1:300, 2:350}
server.data_bank.set_holding_registers(1, [Data[1]])

#DataBank.set_words(2, int(3500));

