import unittest,numpy
# from utilities import getPath,parseNumber,update_json
from .Linear_Algebra import Linear_Algebra
class TDD_LINEAR_ALGEBRA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
        cls.l=Linear_Algebra()
    def test_Linear_Algebra(self):
        l=self.l
        self.assertIsInstance(l.vectors['objects']['Audio signals'],float)
        self.assertIsInstance(l.vectors['objects']['Rn'],tuple)
    def test_Systems_Linear_Equations(self):
        l = self.l
        self.assertRaises(numpy.linalg.LinAlgError,l.linalgSolve,[[1,1,1],[1,-1,2],[2,0,3]],[3,2,1])
        s=l.linalgSolve([[1,1,1],[1,-1,2],[0,1,1]],[3,2,2])
        self.assertEqual(s.tolist(),[1,1,1])
        self.assertRaises(numpy.linalg.LinAlgError,l.linalgSolve,[[1,1,1],[1,-1,2],[2,0,3]],[3,2,5])
        s=l.lstsq([[1,1,1],[1,-1,2],[2,0,3]],[3,2,5])
        Least_squares = s[0].astype(int)
        print(Least_squares)
        self.assertEqual(Least_squares.tolist(),[1,1,1])
if __name__ == '__main__':
    unittest.main()
                