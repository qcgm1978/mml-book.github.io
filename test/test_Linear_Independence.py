import unittest
# from utilities import getPath,parseNumber,update_json
from module.Vectors import Vectors

class TDD_LINEAR_INDEPENDENCE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1

    def test_Linear_Independence(self):
        v = Vectors()
        edge = round(v.get_third_edge(374, 506, 180-45*2))
        self.assertEqual(edge, 752)
        s='''1 3 0
0 0 2 '''
        self.assertTrue(v.is_REF(s))
        self.assertEqual(v.get_Basic_Free(s)[0],['x1','x3'])
        self.assertEqual(v.get_Basic_Free(s)[1], ['x2'])
        self.assertEqual(v.get_linear_combination(s),[(1,2,3,'The 2 column is a non-pivot column because it is 3.0 times the 1 column')])
if __name__ == '__main__':
    unittest.main()
