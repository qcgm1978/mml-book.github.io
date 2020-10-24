import unittest
# from utilities import getPath,parseNumber,update_json
from .Abelian_Group import Abelian_Theory_Group
class TDD_GROUP_THEORY(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
    def test_group_theory(self):
        a = Abelian_Theory_Group([[2,2,3]])
        self.assertEqual(a.Group_Order(),12)
        self.assertEqual(a.Group_Generators(),[[1, 2], [3, 4], [5, 6, 7]])
if __name__ == '__main__':
    unittest.main()
                