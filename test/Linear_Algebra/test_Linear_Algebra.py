import unittest
import numpy as np
from functools import reduce
from test.Linear_Algebra.Linear_Algebra import Linear_Algebra


class TDD_LINEAR_ALGEBRA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1

    def test_Linear_Algebra(self):
        self.assertEqual(self.foo, 1)

    def test_linalg_solve(self):
        la = Linear_Algebra()
        a = np.array([[3, 1], [1, 2]])
        b = np.array([9, 8])
        x = np.linalg.solve(a, b)
        self.assertEqual(x.tolist(), [2.,  3.])
        # s='''x + y + z = 6
        # 2y + 5z = −4
        # 2x + 5y − z = 27'''
        x = np.linalg.solve([[1, 1, 1], [0, 2, 5], [2, 5, -1]], [6, -4, 27])
        self.assertEqual(x.tolist(), [5, 3, -2])
        x = np.linalg.solve([[1, -.2], [1, -.5]], [0, .5*(-6)])
        self.assertEqual(x.tolist(), [2, 10])
        x = np.linalg.solve([[3, 2], [1, 1]], [19, 8])
        self.assertEqual(x.tolist(), [3, 5])
        x = np.linalg.solve([[1, 0, 1], [0, -3, 1], [2, 1, 3]], [6, 7, 15])
        m = x-[2, -1, 4]
        self.assertTrue(m[abs(m)<1e-7].all())
        with self.assertRaises(np.linalg.LinAlgError) as cm:
            np.linalg.solve([[2, -1], [6, -3]], [4, 3])
        self.assertEqual(str(cm.exception), 'Singular matrix')
        with self.assertRaises(np.linalg.LinAlgError) as cm:
            np.linalg.solve([[2, -1], [6, -3]], [4, 12])
        self.assertEqual(str(cm.exception),'Singular matrix')
        x = np.linalg.solve([[1, 1, 1], [0, 2, 5], [2, 5, -1]], [6, -4, 27])
        self.assertEqual(x.tolist(),[5,3,-2])
    def test_matrix_linear(self):
        la = Linear_Algebra()
        m = [[1, 1, 1], [0, 2, 5], [2, 5, -1]]
        r=[6, -4, 27]
        equations=la.convert_equations(m,r)
        self.assertEqual(equations[0],'x+y+z=6')
        self.assertEqual(equations[1],'2y+5z=-4')
        self.assertEqual(equations[2],'2x+5y-z=27')
        x = np.linalg.solve(m, r)
        self.assertEqual(x.tolist(), [5, 3, -2])
        inv = np.linalg.inv(m)
        x=np.dot(inv,r)
        self.assertEqual(np.round(x).tolist(), [5, 3, -2])
    def test_hyperfactorial(self):
        # The fifth hyperfactorial: 5⁵ × 4⁴ × 3³ × 2² × 1¹ = 86400000 milliseconds is exactly 1 day!
        prod = reduce(lambda acc, item: acc*item ** item, [5, 4, 3, 2, 1], 1)
        self.assertEqual(prod, 24*60*60*1000)

    def test_Drake(self):
        # N = R∗fpneflfifcL emperical equation
        pass
    def test_linear_equations(self):
        la = Linear_Algebra()
        la.plot_linear(['2*x+1','(5*x - 6) / 3','2 *( 3 - x)'])


if __name__ == '__main__':
    unittest.main()
