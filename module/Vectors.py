import math,re,numpy as np
from sympy import symbols,lambdify,sqrt
from module.Linear_Algebra import Linear_Algebra

class Vectors(Linear_Algebra):
    def get_vec(self,b,target):
        ret=np.dot(b,np.vstack(target))
        return ret

    # The non-pivot columns can be expressed as linear combinations of the pivot columns on their left.
    def get_linear_combination(self, m):
        B, F,m = self.get_Basic_Free(m)
        ret=[]
        for b, f in zip(B, F):
            i_b=int(re.search(r'\d+$',b).group())
            i_f=int(re.search(r'\d+$',f).group())
            eles_f=m[:,i_f-1]
            ele_f = eles_f[eles_f != 0]
            eles_b=m[:,i_b-1]
            ele_b = eles_b[eles_b != 0]
            e=(i_b,i_f,(ele_f/ele_b).item(0))
            s='The {1} column is a non-pivot column because it is {2} times the {0} column'.format(*e)
            ret.append((*e,s))
        return ret
    # https://www.mathsisfun.com/algebra/trig-solving-sas-triangles.html
    # "SAS" is when we know two sides and the angle between them.
    def get_third_edge(self, s1, s2, A):
        b,c,cosA = symbols('b c cosA')
        f = sqrt(b**2 + c**2 - 2*b*c*cosA)
        fLam = lambdify('b,c,cosA',f)
        cos = math.cos(A)
        return fLam(s1,s2,cos)
        # s='sqrt(b^2 + c^2 − 2bc * cosA)'
        