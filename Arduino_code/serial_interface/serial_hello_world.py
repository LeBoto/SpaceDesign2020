# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:25:46 2017

@author: glassbox
"""

"""Module importation"""
import serial
"""Opening of the serial port"""
try:
    arduino = serial.Serial("COM7", timeout=1)
except:
    print('Please check the port')

"""Receiving data and storing it"""
data = str(arduino.readline())
parsed_data = data.split(',')
