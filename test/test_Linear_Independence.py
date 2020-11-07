import unittest
import numpy as np
from scipy.optimize import fsolve
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
        s = '''1 3 0
0 0 2 '''
        self.assertTrue(v.is_REF(s))
        self.assertEqual(v.get_Basic_Free(s)[0], ['x1', 'x3'])
        self.assertEqual(v.get_Basic_Free(s)[1], ['x2'])
        self.assertEqual(v.get_linear_combination(s), [
                         (1, 2, 3, 'The 2 column is a non-pivot column because it is 3.0 times the 1 column')])

    def test_Linear_Mappings(self):
        v = Vectors()
        standardBasis = np.vstack([[1, 0], [0, 1]])
        altBasis = np.vstack([[1, 1], [-1, 1]])
        target = [2, 3]
        self.assertEqual(
            v.get_vec(standardBasis, target).tolist(), [[2], [3]])
        self.assertEqual(altBasis.tolist(), [[1, 1], [-1, 1]])
        self.assertEqual(np.linalg.solve(
            altBasis, target).tolist(), [-1/2, 5/2])
        self.assertEqual(np.linalg.solve(
            altBasis, target).tolist(), [-1/2, 5/2])
        # self.assertEqual(v.get_solutions(altBasis, target), [-1 / 2, 5 / 2])

    def test_Abelian(self):
        # a⋆b := ab+a+b, a,b ∈ R\{−1}
        l = Vectors()

        def get_e(x):
            return np.eye(x.shape[0])

        def gen_ele(n, m=1):
            limit = l.get_limit()
            if n is None:
                n = limit
            data = np.random.uniform(-limit, limit, (1, 1))
            data[data == 1] = 2
            return data
        def op(x, y):
            return x * y + x + y
        def has_inverse( *args):
            # ab+a+b=1 has R\{−1} solution
            def func(x):
                return [x[0] * x[1]+x[0]+x[1] - 1,
                        0]
            root = fsolve(func, [1, 1])
            return len(root) and -1 not in root
        def is_ele(ele):
            def func(x):
                return [x[0] * x[1]+x[0]+x[1] + 1,
                        0]
            root = fsolve(func, [1, 1])
            return -1 in root
        is_Abelian = l.is_Abelian( get_e=get_e, gen_ele=gen_ele,op=op,has_inverse=has_inverse,is_ele=is_ele)
        self.assertTrue(is_Abelian)
        def solve():
            def func(x):
                return [x[0] * x[1]+x[0]+x[1] - x[2],
                        3*x[2]+x[2]+3-15,0]
            root = fsolve(func, [1, 1,1])
            if - 1 not in root:
                return root
        self.assertFalse((solve()-[1,1,1]).any())

if __name__ == '__main__':
    unittest.main()
