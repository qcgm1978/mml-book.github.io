import sys
import numpy as np


class Linear_Algebra(object):
    underlie = 'vector space'

    @property
    def vectors(self):
        vectors = {
            'properties': ('can be added together', 'multiplied by scalars', 'to produce another object of the same kind'),
            'objects': {
                'geometric': ('concrete'),
                'polynomial': ('concepts'),
                'Audio signals': float(),
                'Rn': (float(),)
            }
        }
        return vectors

    def getYByFunc(self, x, coefs):
        y = np.polyval(coefs, x)
        return y

    def linalgSolve(self, a, b):
        if len(np.array(a).shape) == 1:
            a = [a]
        return np.linalg.solve(a, b)

    def lstsq(self, a, b):
        return np.linalg.lstsq(a, b, rcond=None)

    def dot(self, a, b):
        return np.dot(a, b)

    def is_group(self, gen_ele, get_inv, is_ele, get_e, op, m=1):
        # 1. Closure of G under ⊗: ∀x, y∈G: x⊗y∈G
        # 2. Associativity:∀x,y,z∈G:(x⊗y)⊗z=x⊗(y⊗z)
        # 3. Neutral element: ∃e∈G ∀x∈G: x⊗e=x and e⊗x=x
        # 4. Inverse element:∀x∈G ∃y∈G: x⊗y=e and y⊗x=e
        max_int64 = 9223372036854775807
        n = np.random.randint(2, np.log2(max_int64))
        x = gen_ele(n, m)
        y = gen_ele(n, m)
        z = gen_ele(n, m)
        inv = get_inv(x)
        e = get_e(x)
        is_closure = is_ele(op(x, y))
        round1=np.array(list(map(lambda item:item.round(),op(op(x, y), z))))
        round2=np.array(list(map(lambda item:item.round(),op(x,op(y,z)))))
        is_associa = ~(round1 - round2).any()
        has_neutral = ~(op(x, e) - x).any() and ~(op(e, x) - x).any()
        has_inverse = ~(op(x, inv) - e).any() and ~(op(inv, x) - e).any()
        meet_condition = is_closure and is_associa and has_neutral and has_inverse
        return meet_condition
