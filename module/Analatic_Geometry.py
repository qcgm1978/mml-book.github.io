import math
import numpy as np
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
from sympy import solveset, S,Poly
from sympy.solvers.inequalities import solve_rational_inequalities,reduce_rational_inequalities
import mystic.symbolic as ms
class Analatic_Geometry(object):
    def is_symmetric(self, A, B=None):
        A = np.array(A)
        rows = A.shape[0]
        if len(A.shape) == 2:
            cols = A.shape[1]
        else:
            cols = 0
        if rows != cols:
            A = A[:]
            A = self.get_square_mat(A)
            if A is None:
                return None
        if B is None:
            B = A.T
        minus = (A-B)
        return ~(minus).any()

    @staticmethod
    def get_square_mat(A):
        A = np.array(A)
        rows = A.shape[0]
        sqrt_r = math.isqrt(rows)
        if sqrt_r ** 2 == rows:
            A = A.reshape((sqrt_r, sqrt_r))
        else:
            A = None
        return A

    def is_pos_definite(self, A):
        is_symmetric = self.is_symmetric(A)
        A = self.get_square_mat(A)
        return is_symmetric and np.all(np.linalg.eigvals(A) > 0)