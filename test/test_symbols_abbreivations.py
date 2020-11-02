import unittest
# from utilities import getPath,parseNumber,update_json
from module.Symbols_Abbreviations import *
from module.latex import latex

class TDD_SYMBOLS_ABBREIVATIONS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1

    def test_Constants_Sym_Abbre(self):
        H = Handle_Sym_Abbre()
        # self.assertEqual(len(H.l_sym), 70)

    def test_abbreivations(self):
        get_mean = Handle_Sym_Abbre().get_mean
        self.assertEqual(get_mean('e.g.'),
                         'Exempli gratia(Latin: for example)')
        self.assertEqual(get_mean('SVM'), 'Support vector machine')
        self.assertEqual(get_mean('PCA'), 'Principal component analysis')
        self.assertEqual(get_mean('REF'), 'Row-echelon form')

    def test_symbols(self):
        get_symbol_mean = Handle_Sym_Abbre().get_symbol_meaning
        self.assertEqual(get_symbol_mean('a,b,c,α,β,γ'),
                         'Scalars are lowercase')
        self.assertEqual(get_symbol_mean('A'), 'Matrices are bold uppercase')
        self.assertEqual(get_symbol_mean('Beta(α, β)'),
                         'Beta distribution with parameters α, β')
        self.assertEqual(get_symbol_mean('R'), 'Real numbers')
        self.assertEqual(get_symbol_mean('C'), 'Complex numbers')
        self.assertEqual(get_symbol_mean(
            'Z'), 'Integers')
        self.assertEqual(get_symbol_mean(
            'N'), 'natural numbers Or Number of data points indexed by n = 1,...,N')
        self.assertEqual(get_symbol_mean('Rn'), 'n-dimensional vector space of real numbers, i.e. n-tuples as column vectors')
        self.assertEqual(get_symbol_mean('R5'), 'n-dimensional vector space of real numbers, i.e. n-tuples as column vectors')
        self.assertEqual(get_symbol_mean('Rn×1'), 'n-dimensional vector space of real numbers, i.e. n-tuples as column vectors')
        self.assertEqual(get_symbol_mean(
            'RD'), 'n-dimensional vector space of real numbers, i.e. n-tuples as column vectors')
        self.assertEqual(get_symbol_mean(
            'R3'), 'n-dimensional vector space of real numbers, i.e. n-tuples as column vectors')
        self.assertEqual(get_symbol_mean('x'), 'Vectors are bold lowercase')
        self.assertEqual(get_symbol_mean(
            'λ'), 'Eigenvalue or Lagrange multiplier')
        self.assertEqual(get_symbol_mean(
            '∀A'), 'Universal quantifier: for all x')
        self.assertEqual(get_symbol_mean(
            '∀x,y'), 'Universal quantifier: for all x')
        self.assertEqual(get_symbol_mean('A−1'), 'Inverse of a matrix')
        self.assertEqual(get_symbol_mean(
            'A⊤'), 'Transpose of a vector or matrix')
        self.assertEqual(get_symbol_mean('a=:b'), 'b is defined as a')
        self.assertEqual(get_symbol_mean('a:=b'), 'a is defined as b')
        self.assertEqual(get_symbol_mean(
            'Im'), 'Identity matrix of size m × m')
        self.assertEqual(get_symbol_mean('⇐⇒'), 'If and only if')
        self.assertEqual(get_symbol_mean('∥ · ∥'),
                         'Norm; Euclidean unless specified')
        self.assertEqual(get_symbol_mean(
            '∃e'), 'Existential quantifier: there exists x')
        self.assertEqual(get_symbol_mean('⊗'), 'an group operation')
        self.assertEqual(get_symbol_mean('(Z, +)'),
                         'sets with associated operations')
        self.assertEqual(get_symbol_mean('(N0 , +)'),
                         'sets with associated operations')
        z_mul = get_symbol_mean('(Z, ·)')
        print(z_mul)
        self.assertEqual(z_mul, 'sets with associated operations')
        self.assertEqual(get_symbol_mean('(R, ·)'),
                         'sets with associated operations')
        self.assertEqual(get_symbol_mean(
            '(R\{0}, ·)'), 'sets with associated operations')
        self.assertEqual(get_symbol_mean('(Rm×n , +)'),
                         'sets with associated operations')
        self.assertEqual(get_symbol_mean('(V , +, ·)'),'a set with two operations')
        self.assertEqual(get_symbol_mean('\\{0}'),'excluding number')
        self.assertEqual(get_symbol_mean('GL(n, R)'),'general linear group')
        self.assertEqual(get_symbol_mean('G × G → G'),'sets G and inner|outer operations on G')
        self.assertEqual(get_symbol_mean('V×V→V'),'sets G and inner|outer operations on G')
        self.assertEqual(get_symbol_mean('R×V→V'),'sets G and inner|outer operations on G')
        
    def test_matrix(self):
        get_symbol_mean = Handle_Sym_Abbre().get_symbol_meaning
        self.assertEqual(get_symbol_mean('(1, n)-matrices '),'rows/columns; row/column vectors')
        self.assertEqual(get_symbol_mean('(m, 1)-matrices'),'rows/columns; row/column vectors')
        self.assertEqual(get_symbol_mean('Rm×n'),'the set of all real-valued (m, n)-matrices')
        self.assertEqual(get_symbol_mean('R_n'),'indicate the nth Row')
        self.assertEqual(get_symbol_mean('R_1'),'indicate the nth Row')
        self.assertEqual(get_symbol_mean('A ∈ Rm×n'),'the set of all real-valued (m, n)-matrices')
        self.assertEqual(get_symbol_mean('a ∈ Rmn'),'stacking all n columns of the matrix into a long vector')
        self.assertEqual(get_symbol_mean('⟨x,y⟩'),'Inner product of x and y')
        self.assertEqual(get_symbol_mean('a⊤b'),'the dot product between two vectors a, b')
        self.assertEqual(get_symbol_mean('A · B'),'multiplication (explicitly showing “·”)')
        self.assertEqual(get_symbol_mean('Rn×n'),'identity matrix i.e. the n × n-matrix containing 1 on the diagonal and 0 everywhere else')
        self.assertEqual(get_symbol_mean('\rightsquigarrow'),'a transformation of the augmented matrix using elementary transformations')
        self.assertEqual(get_symbol_mean('[A | b]'), 'The augmented matrix [A | b] compactly represents the system of linear equations Ax = b')
    def test_set_symbols(self):
        g = Handle_Sym_Abbre().get_symbol_meaning
        self.assertEqual(g('span[b1 ]'),'Span (generating set) of b1')
        self.assertEqual(g('span[A]'),'Span (generating set) of b1')
        self.assertEqual(g('span[x1,...,xk]'),'Span (generating set) of b1')
        self.assertEqual(g('\subseteq'),'is subset of')
        self.assertEqual(g('U ⊆ V'),'a subspace U of V')
        self.assertEqual(g('\subsetneq'), 'A is a proper (or strict) subset of B')
        self.assertEqual(g('∅'),'Empty set')
    def test_sym_properties(self):
        p = Handle_Sym_Abbre().get_sym_properties
        self.assertCountEqual(p('(V , +, ·)'), {'V': 'Vecotors', 'meaning': 'a set with two operations', 'neutral_element':
                                                '0 = [0, . . . , 0]⊤', 'inner_operation': '+ called vector addition', 'outer_operation': '· multiplication by scalars'})
    def test_latex(self):
        self.assertEqual(latex['\in'],'is member of')

if __name__ == '__main__':
    unittest.main()
