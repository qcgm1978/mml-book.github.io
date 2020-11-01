import unittest
# from utilities import getPath,parseNumber,update_json
from module.Vectors import Vectors
from module.Linear_Algebra import Linear_Algebra

class TDD_LINEAR_INDEPENDENCE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1

    def test_Linear_Independence(self):
        v = Vectors()
        l=Linear_Algebra()
        edge = round(v.get_third_edge(374, 506, 180-45*2))
        self.assertEqual(edge, 752)
        s='''1 3 0
0 0 2 '''
        self.assertTrue(l.is_REF(s))
        self.assertEqual(l.get_Basic_Free(s)[0],['x1','x3'])
        self.assertEqual(l.get_Basic_Free(s)[1],['x2'])

if __name__ == '__main__':
    unittest.main()
