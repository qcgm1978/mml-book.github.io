import math,re
from sympy import symbols,lambdify,sqrt
from module.Linear_Algebra import Linear_Algebra

class Vectors(Linear_Algebra):
    # The non-pivot columns can be expressed as linear combinations of the pivot columns on their left.
    def get_linear_combination(self, m):
        B, F = self.get_Basic_Free(m)
        ret=[]
        for b, f in zip(B, F):
            i_b=re.search(r'\d+$',b).group()
            i_f=re.search(r'\d+$',f).group()
            ret.append((int(i_b), int(i_f)))
        return ret
    # https://www.mathsisfun.com/algebra/trig-solving-sas-triangles.html
    # "SAS" is when we know two sides and the angle between them.
    def get_third_edge(self, s1, s2, A):
        b,c,cosA = symbols('b c cosA')
        f = sqrt(b**2 + c**2 - 2*b*c*cosA)
        fLam = lambdify('b,c,cosA',f)
        f
        cos = math.cos(A)
        return fLam(s1,s2,cos)
        # s='sqrt(b^2 + c^2 − 2bc * cosA)'
        