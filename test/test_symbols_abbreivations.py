import unittest
# from utilities import getPath,parseNumber,update_json
from .Symbols_Abbreviations import *


class TDD_SYMBOLS_ABBREIVATIONS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
    def test_Constants_Sym_Abbre(self):
        H = Handle_Sym_Abbre()
        self.assertEqual(len(H.l_sym),68)
    def test_abbreivations(self):
        get_mean=Handle_Sym_Abbre().get_mean
        self.assertEqual(get_mean('e.g.'),
                         'Exempli gratia(Latin: for example)')
        self.assertEqual(get_mean('SVM'), 'Support vector machine')
        self.assertEqual(get_mean('PCA'), 'Principal component analysis')
        self.assertEqual(get_mean('REF'), 'Row-echelon form')

    def test_symbols(self):
        get_symbol_mean=Handle_Sym_Abbre().get_symbol_meaning
        self.assertEqual(get_symbol_mean('a,b,c,α,β,γ'),
                         'Scalars are lowercase')
        self.assertEqual(get_symbol_mean('A'), 'Matrices are bold uppercase')
        self.assertEqual(get_symbol_mean('Beta(α, β)'),
                         'Beta distribution with parameters α, β')
        self.assertEqual(get_symbol_mean(
            'R'), 'Real and complex numbers, respectively')
        self.assertEqual(get_symbol_mean(
            'Z'), 'Integers')
        self.assertEqual(get_symbol_mean('N'), 'natural numbers Or Number of data points; indexed by n = 1,...,N')
        self.assertEqual(get_symbol_mean(
            'Rn'), 'n-dimensional vector space of real numbers')
        self.assertEqual(get_symbol_mean(
            'RD'), 'n-dimensional vector space of real numbers')
        self.assertEqual(get_symbol_mean(
            'R3'), 'n-dimensional vector space of real numbers')
        self.assertEqual(get_symbol_mean('x'), 'Vectors are bold lowercase')
        self.assertEqual(get_symbol_mean(
            'λ'), 'Eigenvalue or Lagrange multiplier')
        self.assertEqual(get_symbol_mean(
            '∀A'), 'Universal quantifier: for all x')
        self.assertEqual(get_symbol_mean('A−1'), 'Inverse of a matrix')
        self.assertEqual(get_symbol_mean(
            'A⊤'), 'Transpose of a vector or matrix')
        self.assertEqual(get_symbol_mean('=:'), 'b is defined as a')
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
        self.assertEqual(z_mul,'sets with associated operations')
        self.assertEqual(get_symbol_mean('(R, ·)'),'sets with associated operations')
        self.assertEqual(get_symbol_mean('(R\{0}, ·)'),'sets with associated operations')
        self.assertEqual(get_symbol_mean('(Rm×n , +)'),'sets with associated operations')
        self.assertEqual(get_symbol_mean('(V , +, ·)'),'a set with two operations')
    def test_sym_properties(self):
        p=Handle_Sym_Abbre().get_sym_properties
        self.assertCountEqual(p('(V , +, ·)'),{'V': 'Vecotors', 'meaning': 'a set with two operations','neutral_element': '0 = [0, . . . , 0]⊤','inner_operation':'+ called vector addition','outer_operation': '· multiplication by scalars'})


if __name__ == '__main__':
    unittest.main()
