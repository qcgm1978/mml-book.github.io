import sys
import re
import numpy as np
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve

class Linear_Algebra(object):
    underlie = 'vector space'
    op=np.add
    def __init__(self):
        power = 8
        self.m=np.random.randint(2**-power-1,2**power-1)
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
    def convert_s(self, s):
        s = re.sub(r'􀀀', '-', s)
        s = re.split(r'\n', s.strip())
        ret=[]
        for index,item in enumerate(s):
            ret.append([])
            l = re.split(r'\s+', item)
            cols=len(l)
            for ind, it in enumerate(l):
                next_it=pre_it=None
                if ind<cols-1:
                    next_it=l[ind + 1]
                if ind:
                    pre_it=l[ind - 1]
                if next_it == '+':
                    ret[-1].append(it + next_it + l[ind + 2])
                elif it == '+' or pre_it == '+':
                    continue
                else:
                    try:
                        ele = int(it)
                    except ValueError:
                        ele=it
                    ret[-1].append(ele)
        return ret
    def get_REF(self, augmented_m):
        if isinstance(augmented_m, str):
            augmented_m=self.convert_s(augmented_m)
        return augmented_m
    def get_solutions(self, m,is_augumented=False):
        if isinstance(m, str):
            m = self.convert_s(m)
        m=np.mat(m)
        if is_augumented:
            m = m[:,:-1]
        m=m.astype(np.int8)
        basic, free,_ = self.get_Basic_Free(m)
        ind_free = list(map(lambda item: int(
            re.search(r'\d+$', item).group()) - 1, free))
        sol = np.zeros((len(ind_free), m.shape[1]), dtype=np.int8)
        for index, item in enumerate(ind_free):
            col = m[:, item].getA1()
            row_free = [i for i, it in enumerate(col) if it not in [1, 0]]
            for row in row_free:
                for ind in range(item-1, -1, -1):
                    if m[row, ind] == 1:
                        sol[index, ind] = m[row, item]
                        sol[index, item] = -1
                        break
        latex = self.get_latex(sol)
        return sol, latex

    def get_latex(self, sol):
        pre = r'''$\left\{{\boldsymbol{{x}} \in \mathbb{{R}}^{{{0}}}: \boldsymbol{{x}}='''.format(sol.shape[1])
        post = r''' \in \mathbb{R}\right\}$'''
        lam = [r'''\lambda_{{{0}}}'''.format(item + 1) for item in range(sol.shape[0])]
        lams=', '.join(lam)
        eles = r''', \quad '''+lams
        s = [r'''\lambda_{{{0}}}\left[\begin{{array}}{{c}}{1}\end{{array}}\right]'''.format(
            index+1, r' \\ '.join(item.astype(str))) for index, item in enumerate(sol)]
        vectors = '+'.join(s)
        cols = vectors+eles
        latex = pre+cols+post
        return latex
    # It is in row-echelon form.
    # Every pivot is 1.
    # The pivot is the only nonzero entry in its column.

    def is_reduced_echelon(self, m):
        m = np.mat(m)
        echelon = self.get_Basic_Free(m)
        if echelon:
            basic = map(lambda item: re.search(
                r'\d+$', item).group(), echelon[0])
            for item in basic:
                col = m[:, int(item) - 1]
                length = len(col[col != 0])
                if length > 1:
                    return False
            return True
        else:
            return False
    # All rows that contain only zeros are at the bottom of the matrix
    # the first nonzero number from the left (also called the pivot or the leading coefficient) is always strictly to the right of the pivot of the row above it
    def is_REF(self, m, is_augumented=False):
        if isinstance(m, str):
            m=self.convert_s(m)
        m = np.mat(m)
        if is_augumented:
            m = m[:,:-1]
        m=m.astype(np.int8)
        ind = -1
        cols = m.shape[1]
        for index, row in enumerate(m):
            zeros = 0
            for item in row.getA1():

                if item:
                    break
                zeros += 1
            if zeros == cols:
                following = m[index+1:]
                if not following.size or all(following[following == 0]):
                    return True

            elif zeros >= ind + 1 :
                ind = zeros
                continue
            else:
                return False
        return True
    # The variables corresponding to the pivots in the row-echelon form are called basic variables and the other variables are free variables
    def get_Basic_Free(self,m):
        if isinstance(m, str):
            m=self.convert_s(m)
        m=np.mat(m)
        Basic = []
        Free = []
        for index, row in enumerate(m):
            is_last = index + 1 == m.shape[0]
            ini=True
            for i, item in enumerate(row.getA1()):
                v = 'x{0}'.format(i + 1)
                if item :
                    if v not in Basic and ini:
                        Basic.append(v)
                        ini=False
                        if not is_last:
                            break
                    elif is_last and v not in Free:

                        Free.append(v)
                else:
                    if is_last and v not in Basic:
                        Free.append(v)
        return Basic, Free,m
    @staticmethod
    def gen_ele(n, m=1):
        power = 4
        r = np.random.randint(2**-power-1,
                                2**power-1, (m, n))
        p = np.random.randint(2**-power-1, 2**power-1)
        return (r ** 10 ** p).round()

    @staticmethod
    def get_inv(x):
        return - x

    @staticmethod
    def is_ele(ele):
        return ele.dtype == 'int64'
    @staticmethod
    def is_float(ele):
            return ele.dtype == 'float64'
    @staticmethod
    def get_e(Zn):
        return np.zeros(len(Zn[0]))
        
    def is_Abelian(self, **kwarg):
        m = kwarg['m'] if 'm' in kwarg else self.m
        op=kwarg['op'] if 'op' in kwarg else self.op
        gen_ele=kwarg['gen_ele'] if 'gen_ele' in kwarg else self.gen_ele
        
        n = m
        is_group = self.is_group(
            **kwarg)
        x = gen_ele(n, m)
        y = gen_ele(n, m)
        # ∀x,y∈G:x⊗y=y⊗x,then G=(G,⊗)is an Abelian group (commutative)
        data = op(x, y) - op(y, x)
        is_commutative=data[:]< 1e-7
        return is_group and is_commutative 

    def get_limit(self):
        max_int64 = 9223372036854775807
        n = np.random.randint(2, np.log2(max_int64))
        return n
    @staticmethod
    def solve_nonlinear(*args):
        return nonlinsolve(*args)
    @staticmethod
    def get_sym_var(s):
        x, y = symbols(s, real=True)
        return x, y
    def is_group(self, gen_ele=None, is_ele=None, n=None, has_inverse=None, m=1, op=np.add, get_inv=None,get_e=None,associa=None):
        if get_e is None:
            get_e=self.get_e
        if gen_ele is None:
            gen_ele = self.gen_ele
        if get_inv is None:
            get_inv=self.get_inv
        if is_ele is None:
            is_ele=self.is_ele
        if has_inverse is None:
            has_inverse = self.has_inverse
        # 1. Closure of G under ⊗: ∀x, y∈G: x⊗y∈G
        # 2. Associativity:∀x,y,z∈G:(x⊗y)⊗z=x⊗(y⊗z)
        # 3. Neutral element: ∃e∈G ∀x∈G: x⊗e=x and e⊗x=x
        # 4. Inverse element:∀x∈G ∃y∈G: x⊗y=e and y⊗x=e
        if n is None:
            n = self.get_limit()
        x = gen_ele(n, m)
        y = gen_ele(n, m)
        z = gen_ele(n, m)
        inv = get_inv(x)
        e = self.get_e(x)
        is_closure = is_ele(op(x, y))
        if callable(associa):
            is_associa =associa(x,y,z)
        else:
            round1 = np.array(
                list(map(lambda item: item.round(), op(op(x, y), z))))
            round2 = np.array(
                list(map(lambda item: item.round(), op(x, op(y, z)))))
            is_associa = ~(round1 - round2).any()
        has_neutral = self.has_inverse(x, e, x,op)
        has_inverse = has_inverse(x, inv, e)
        meet_condition = is_closure and is_associa and has_neutral and has_inverse
        return meet_condition
    @staticmethod
    def has_inverse( x, inv, e,op = np.add):
        return ~(op(x, inv) - e).any() and ~(op(inv, x) - e).any()

    def get_invtible(self, n=None):
        if n is None:
            n = self.get_limit()
        m = np.random.uniform(-1, 1, (n, n))
        d = np.dot(m, m.T)
        return d

    def is_invtible(self, m):
        inv = np.linalg.inv(m)
        d = np.dot(m, inv)
        return np.allclose(d, np.eye(m.shape[0]))
