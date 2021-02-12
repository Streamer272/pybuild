import unittest
import subprocess


class MyTestCase(unittest.TestCase):
    def test_pm(self):
        self.assertEqual(
            subprocess.check_output("C:\\Users\\danko\\AppData\\Local\\Programs\\Python\\Python39\\python.exe D:/Desktop/Coding/Python/PyManager/src/pm.py add_modules D:\\Desktop\\Coding\\Python\\test"),
            "Cloning module tkinter...\r\nModule tkinter cloned\r\n".encode())


if __name__ == '__main__':
    unittest.main()
