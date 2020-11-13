import unittest
from module.Analatic_Geometry import Analatic_Geometry
class TDD_ANALATIC_GEOMETRY(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
    def test_Analatic_Geometry(self):
        a=Analatic_Geometry()
        A1 = [9, 6, 6, 5]
        A2=[9,6,6,3]
        self.assertTrue(a.is_symmetric(A1))
        self.assertTrue(a.is_symmetric(A2))
        self.assertTrue(a.is_pos_definite(A1))
        self.assertFalse(a.is_pos_definite(A2))
if __name__ == '__main__':
    unittest.main()
                