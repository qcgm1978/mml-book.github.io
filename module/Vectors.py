import math
from sympy import *

class Vectors(object):
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
        