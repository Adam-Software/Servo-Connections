#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scservo_sdk import *
import logging

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Connection(metaclass=MetaSingleton):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.DEBUG)

    _BAUDRATE = 1000000
    _DEVICENAME = '/dev/ttyUSB0'
    _portHandler = None
    _packetHandler = None

    def _initPortHandler(self):
        if self._portHandler is None:
            self._portHandler = PortHandler(self._DEVICENAME)
            self._openPort()

    def _initPacketHandler(self):
        if self._packetHandler is None:
            self._packetHandler = sms_sts(self._portHandler)
            #self._packetHandler =  scscl(self._portHandler) 
            self._setBaudrate()

    def _setBaudrate(self):
        if self._portHandler.setBaudRate(self._BAUDRATE):
            logging.info("Succeeded to change the baudrate")

    def _openPort(self):
        if self._portHandler.openPort():
            logging.info("Succeeded to open the port")

    def getPortHandler(self):
        if self._portHandler is None:
            self._initPortHandler()

        return self._portHandler

    def getPacketHandler(self):
        if self._packetHandler is None:
            self._initPortHandler()
            self._initPacketHandler()

        return self._packetHandler

    def closePort(self):
        if self._portHandler is not None:
            self._portHandler.closePort()

if __name__=='__main__':
    connect1 = Connection().getPacketHandler()
    connect1.closePort()

    connect2 = Connection().getPacketHandler()
    connect3 = Connection().getPacketHandler()
    connect4 = Connection().getPacketHandler()
    connect5 = Connection().getPacketHandler()

    print("Connection Objects 1", connect1)
    print("Connection Objects 2", connect2)
    print("Connection Objects 3", connect3)
    print("Connection Objects 4", connect4)
    print("Connection Objects 5", connect5)
