import unittest
from servo_serial.connection import Connection
#from scservo_sdk import *

class MyTestCase(unittest.TestCase):

    SCSCL_PRESENT_VOLTAGE      = 62
    SCS_ID                     = 13
    scs_end                    = 0

    packetHandler = Connection().getPacketHandler()
    portHandler = Connection().getPortHandler()

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_close_port(self):
        Connection().closePort()
        self.assertEqual(self.packetHandler, None)

if __name__ == '__main__':
    unittest.main()
