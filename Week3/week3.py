# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:40:03 2022

@author: HP
"""

import string

alphabet = " " + string.ascii_lowercase

positions = {}

for c in alphabet:
    positions[c] = alphabet.index(c)

message = "hi my name is caesar"
encoded_message = str()

for _ in message:
    for key, values in positions.items():
        if values == (positions[_] + 3)%27:
            encoded_message += key

print(encoded_message)
