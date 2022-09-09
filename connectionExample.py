#!/usr/bin/env python
# -*- coding: utf-8 -*-

from servo_serial.connection import Connection
from scservo_sdk import *

class ConnectionExample():

    SCSCL_PRESENT_VOLTAGE      = 62
    SCS_ID                     = 13
    scs_end                    = 0

    packetHandler = Connection().getPacketHandler()
    portHandler = Connection().getPortHandler()

    def getVoltage(self):
        scs_present_voltage_speed, scs_comm_result, scs_error = self.packetHandler.read4ByteTxRx(self.SCS_ID, self.SCSCL_PRESENT_VOLTAGE)
        print(scs_present_voltage_speed)

        if scs_comm_result != COMM_SUCCESS:
           print(self.packetHandler.getTxRxResult(scs_comm_result))

        elif scs_error != 0:
            print(self.packetHandler.getRxPacketError(scs_error))

        scs_present_voltage = protocol_packet_handler.scs_makeword(self, scs_present_voltage_speed, scs_comm_result)
        print(scs_present_voltage)

        percent_voltage = ((scs_present_voltage - 92)/(125 - 92))*100

        intvol = int(percent_voltage)
        return intvol


voltage = ConnectionExample().getVoltage()
print(voltage)
