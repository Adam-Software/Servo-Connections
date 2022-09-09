import unittest
from servo_serial.connection import Connection


class MyTestCase(unittest.TestCase):

    def test_similarity_class_instances(self):
        connect1 = Connection()
        connect2 = Connection()
        self.assertEqual(connect1, connect2)

    def test_not_init_close_port(self):
        connect = Connection()
        self.assertEqual(connect.closePort(), None)


if __name__ == '__main__':
    unittest.main()
