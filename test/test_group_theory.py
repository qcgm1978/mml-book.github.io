import unittest
import numpy as np
# from utilities import getPath,parseNumber,update_json
from module.Abelian_Group import Abelian_Theory_Group
from module.Linear_Algebra import Linear_Algebra


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

        
        # (Rn , +), (Zn , +), n ∈ N are Abelian if + is defined componentwise
        la = Linear_Algebra()
        is_group = la.is_group()
        is_Abelian = la.is_group()
        self.assertTrue(is_group)
        self.assertTrue(is_Abelian)

        def gen_ele(n, m=1):
            power = 2
            r = np.random.uniform(2**-power-1,
                                  2**power-1, (m, n))
            return r

        
        # (Rn , +), (Zn , +), n ∈ N are Abelian if + is defined componentwise
        is_group = la.is_group(gen_ele=gen_ele, is_ele=la.is_float)
        is_Abelian = la.is_group(gen_ele=gen_ele, is_ele=la.is_float)
        self.assertTrue(is_group)
        self.assertTrue(is_group)
        # (Rm×n , +), the set of m × n-matrices is Abelian (with componentwise addition

        def gen_ele(n, m=1):
            power = 2
            r = np.random.uniform(2**-power-1,
                                  2**power-1, (m, n))
            return r
        is_group = la.is_group(gen_ele, la.is_float)
        # If the inverse exists (A is regular), then A−1 is the inverse element of A ∈ Rn×n , and in exactly this case (Rn×n , ·) is a group, called the general linear group
        def get_e(x):
            return np.eye(x.shape[0])
        is_Abelian = la.is_Abelian( is_ele=la.is_float, get_e=get_e)
        self.assertTrue(is_group)
        inv = la.get_invtible()
        self.assertTrue(la.is_invtible(inv))
    def test_congruence_classes_modulo(self):
        
if __name__ == '__main__':
    unittest.main()
