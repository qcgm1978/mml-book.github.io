import unittest
# from utilities import getPath,parseNumber,update_json
from Symbols_Abbreviations import *
class TDD_SYMBOLS_ABBREIVATIONS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
    def test_symbols_abbreivations(self):
        self.assertEqual(get_mean('e.g.'),'Exempli gratia(Latin: for example)')
        self.assertEqual(get_mean('SVM'),'Support vector machine')
        self.assertEqual(get_mean('PCA'),'Principal component analysis')
        self.assertEqual(get_symbol_mean('a,b,c,α,β,γ'),'Scalars are lowercase')
        self.assertEqual(get_symbol_mean('A'),'Matrices are bold uppercase')
        self.assertEqual(get_symbol_mean('Beta(α, β)'),'Beta distribution with parameters α, β')
        self.assertEqual(get_symbol_mean('R'),'Real and complex numbers, respectively')
        self.assertEqual(get_symbol_mean('Rn'),'n-dimensional vector space of real numbers')
        self.assertEqual(get_symbol_mean('RD'),'n-dimensional vector space of real numbers')
        self.assertEqual(get_symbol_mean('R3'),'n-dimensional vector space of real numbers')
        self.assertEqual(get_symbol_mean('x'),'Vectors are bold lowercase')
        self.assertEqual(get_symbol_mean('λ'),'Eigenvalue or Lagrange multiplier')
        self.assertEqual(get_symbol_mean('∀A'),'Universal quantifier: for all x')
        self.assertEqual(get_symbol_mean('A−1'),'Inverse of a matrix')
        self.assertEqual(get_symbol_mean('A⊤'),'Transpose of a vector or matrix')
        self.assertEqual(get_symbol_mean('=:'),'b is defined as a')
if __name__ == '__main__':
    unittest.main()
                