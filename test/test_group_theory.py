import unittest
import numpy as np
# from utilities import getPath,parseNumber,update_json
from test.Abelian_Group import Abelian_Theory_Group
from test.Linear_Algebra import Linear_Algebra


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

        def gen_ele(n, m=1):
            power = 4
            r = np.random.randint(2**-power-1,
                                  2**power-1, (m, n))
            p = np.random.randint(2**-power-1, 2**power-1)
            return (r ** 10 ** p).round()

        def get_inv(x):
            return - x

        def is_ele(ele):
            return ele.dtype == 'int64'

        def get_e(Zn):
            return np.zeros(len(Zn[0]))
        op = np.add
        # (Rn , +), (Zn , +), n ∈ N are Abelian if + is defined componentwise
        la = Linear_Algebra()
        is_group = la.is_group(gen_ele, get_inv, is_ele, get_e, op)
        is_Abelian = la.is_group(gen_ele, get_inv, is_ele, get_e, op)
        self.assertTrue(is_group)
        self.assertTrue(is_Abelian)

        def gen_ele(n, m=1):
            power = 2
            r = np.random.uniform(2**-power-1,
                                  2**power-1, (m, n))
            return r

        def is_ele(ele):
            return ele.dtype == 'float64'
        # (Rn , +), (Zn , +), n ∈ N are Abelian if + is defined componentwise
        is_group = la.is_group(gen_ele, get_inv, is_ele, get_e, op)
        is_Abelian = la.is_group(gen_ele, get_inv, is_ele, get_e, op)
        self.assertTrue(is_group)
        self.assertTrue(is_group)
        # (Rm×n , +), the set of m × n-matrices is Abelian (with componentwise addition

        def gen_ele(n, m=1):
            power = 2
            r = np.random.uniform(2**-power-1,
                                  2**power-1, (m, n))
            return r
        power = 8
        m=np.random.randint(2**-power-1,2**power-1)
        is_group = la.is_group(gen_ele, get_inv, is_ele, get_e, op, m=m)
        # If the inverse exists (A is regular), then A−1 is the inverse element of A ∈ Rn×n , and in exactly this case (Rn×n , ·) is a group, called the general linear group
        op = np.dot
        def get_e(x):
            return np.eye(x.shape[0])
        is_Abelian = la.is_Abelian(gen_ele, get_inv, is_ele, get_e, op,m=m)
        self.assertTrue(is_group)
        self.assertFalse(is_Abelian)
        inv = la.get_invtible()
        self.assertTrue(la.is_invtible(inv))
        def gen_ele(n, m=1):
            mat=la.get_invtible(m)
            return mat
        # todo to optimization to reduce params and add general linear group check
        # is_Abelian = la.is_Abelian(gen_ele, get_inv, is_ele, get_e, op,m=m,has_inverse=la.is_invtible)
        # self.assertTrue(is_Abelian)

if __name__ == '__main__':
    unittest.main()
