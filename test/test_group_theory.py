import unittest
import numpy as np
# from utilities import getPath,parseNumber,update_json
from .Abelian_Group import Abelian_Theory_Group
from .Linear_Algebra import Linear_Algebra


class TDD_GROUP_THEORY(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1

    def test_group_theory(self):
        a = Abelian_Theory_Group([[2, 2, 3]])
        self.assertEqual(a.Group_Order(), 12)
        self.assertEqual(a.Group_Generators(), [[1, 2], [3, 4], [5, 6, 7]])

    def test_Abelian(self):
        # (Rn , +), (Zn , +), n ∈ N are Abelian if + is defined componentwise
        # Inverse element:∀x∈G ∃y∈G : x⊗y=e and y⊗x=e,where e is
        # the neutral element.
        Rn = np.array([1, 2, 3])
        e = np.zeros(len(Rn))
        self.assertTrue((Rn+e).tolist() == (e+Rn).tolist() == Rn.tolist())
        # (x1, · · · , xn)−1 := (−x1, · · · , −xn) is the inverse element
        neg_Rn = e - Rn
        self.assertEqual(neg_Rn.tolist(), [-1, -2, -3])
        self.assertEqual((Rn+neg_Rn).tolist(), e.tolist())

        def gen_ele(n):
            power = 4
            r = np.random.randint(2**-power-1,
                                  2**power-1, (1, n))
            p = np.random.randint(2**-power-1, 2**power-1)
            return (r ** 10 ** p).round()

        def get_inv(x):
            return - x

        def is_ele(ele):
            return ele.dtype=='int64'

        def get_e(Zn):
            return np.zeros(len(Zn))
        op = np.add
        # (Rn , +), (Zn , +), n ∈ N are Abelian if + is defined componentwise
        is_group = Linear_Algebra().is_group(gen_ele, get_inv, is_ele, get_e, op)
        self.assertTrue(is_group)
        def gen_ele(n):
            power = 2
            r = np.random.uniform(2**-power-1,
                                  2**power-1, (1, n))
            p = np.random.randint(2**-power-1, 2**power-1)
            return (r ** 10 ** p).round()

        def get_inv(x):
            return - x

        def is_ele(ele):
            return ele.dtype=='float64'

        def get_e(Zn):
            return np.zeros(len(Zn))
        op = np.add
        # (Rn , +), (Zn , +), n ∈ N are Abelian if + is defined componentwise
        is_group = Linear_Algebra().is_group(gen_ele, get_inv, is_ele, get_e, op)
        self.assertTrue(is_group)


if __name__ == '__main__':
    unittest.main()
