import unittest
import sys
sys.path.append("app")
from AltasBajas import AltasBajas

class TestLogin(unittest.TestCase):
    
    def testAgregaUsuario(self):
        altasBajas = AltasBajas()
        self.assertEqual("Paciente agregado", altasBajas.alta("Jose","Roblez","45","holaaa@gmail.com","Abedules #9"))
    
    def testEliminarUsuario(self):
        altasBajas = AltasBajas()
        self.assertEqual("Paciente eliminado", altasBajas.baja("100"))
        
if __name__ == '__main__':
    unittest.main()
