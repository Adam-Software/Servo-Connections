import logging
import unittest
from servo_serial.connection import Connection


class ConnectTestCase(unittest.TestCase):

    def testSimilarityClassInstances(self):
        connect1 = Connection()
        connect2 = Connection()
        self.assertEqual(connect1, connect2)

    def testNotInitClosePort(self):
        connect = Connection()
        self.assertEqual(connect.closePort(), False)

    def testInitClosePort(self):
        connect = Connection()
        connect.getPacketHandler()
        self.assertEqual(connect.closePort(), True)

    def testDefaultLoglevel(self):
        connect = Connection()
        level = connect.getLoggingLevel()
        self.assertEqual(level, logging.ERROR)

    def testChangeLoglevel(self):
        connect = Connection()
        targetLevel = logging.INFO
        connect.setLogginLevel(targetLevel)
        self.assertEqual(connect.getLoggingLevel(), targetLevel)



if __name__ == '__main__':
    unittest.main()
