import unittest
from servo_serial.connection import Connection


class MyTestCase(unittest.TestCase):

    def similarity_test_of_class_instances(self):
        connect1 = Connection()
        connect2 = Connection()
        self.assertEqual(connect1, connect2)

    def test_close_port(self):
        connect = Connection()
        connect.getPacketHandler()
        connect.closePort()
        self.assertEqual(connect.getPacketHandler(), None)


if __name__ == '__main__':
    unittest.main()
