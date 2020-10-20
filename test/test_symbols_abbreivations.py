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
        self.assertEqual(get_symbol_mean('a,b,c,α,β,γ'),'Scalars are lowercase')
        self.assertEqual(get_symbol_mean('Beta(α, β)'),'Beta distribution with parameters α, β')
if __name__ == '__main__':
    unittest.main()
                