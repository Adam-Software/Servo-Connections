import logging
import unittest
from servo_serial.connection import Connection


class ConnectTestCase(unittest.TestCase):

    def testSimilarityClassInstances(self):
        connect1 = Connection()
        connect2 = Connection()
        self.assertEqual(connect1, connect2)

        connect1.closePort()
        connect2.closePort()

    def testNotInitClosePort(self):
        connect = Connection()
        self.assertEqual(connect.closePort(), False)
        connect.closePort()

    def testInitClosePort(self):
        connect = Connection()
        connect.getPacketHandler()
        self.assertEqual(connect.closePort(), True)
        connect.closePort()

    def testDefaultLoglevelAndChangeLogLevel(self):
        connect = Connection()
        level = connect.getLoggingLevel()
        self.assertEqual(level, logging.ERROR)
        targetLevel = logging.INFO
        connect.setLogginLevel(targetLevel)
        self.assertEqual(connect.getLoggingLevel(), targetLevel)
        connect.closePort()


if __name__ == '__main__':
    unittest.main()
