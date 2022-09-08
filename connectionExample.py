from connection import Connection
from scservo_sdk import *

class ConnectionExample():

    SCSCL_PRESENT_VOLTAGE      = 62
    SCS_ID                     = 13

    packetHandler = Connection().getPacketHandler()
    portHandler = Connection().getPortHandler()

    scs_present_voltage_speed, scs_comm_result, scs_error = packetHandler.read4ByteTxRx(self.portHandler, SCS_ID, SCSCL_PRESENT_VOLTAGE)

    def getVoltage(self):
        if scs_comm_result != COMM_SUCCESS:
           print(self.packetHandler.getTxRxResult(scs_comm_result))

        elif scs_error != 0:
            print(self.packetHandler.getRxPacketError(scs_error))

        scs_present_voltage = SCS_MAKEWORD(scs_present_voltage_speed, scs_comm_result)
        percent_voltage = ((scs_present_voltage - 92) / (125 - 92)) * 100

        intvol = int(percent_voltage)
        return intvol

if __name__ == 'main':
    voltage = ConnectionExample().getVoltage()