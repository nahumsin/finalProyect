import unittest
import sys
sys.path.append("app")
from Login import Login


class TestLogin(unittest.TestCase):

    def testUsuarioCorrecto(self):
        login = Login()
        self.assertEqual("True", login.verificar("juanPerez", "cartmancuco"))

    def testUsuaioIncorrecto(self):
        login = Login()
        self.assertEqual(
            "False", login.verificar("juanitoMartinez", "noExisto"))

if __name__ == '__main__':
    unittest.main()
