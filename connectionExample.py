from connection import Connection
from scservo_sdk import *

SCSCL_PRESENT_VOLTAGE      = 62
SCS_ID                     = 13

packetHandler = Connection.getPacketHandler()
scs_present_voltage_speed, scs_comm_result, scs_error = packetHandler.read4ByteTxRx(portHandler, SCS_ID,
                                                                                    SCSCL_PRESENT_VOLTAGE)
if scs_comm_result != COMM_SUCCESS:
    print(packetHandler.getTxRxResult(scs_comm_result))

elif scs_error != 0:
    print(packetHandler.getRxPacketError(scs_error))

scs_present_voltage = SCS_MAKEWORD(scs_present_voltage_speed, scs_comm_result)
percent_voltage = ((scs_present_voltage - 92) / (125 - 92)) * 100

intvol = int(percent_voltage)
print(intvol)