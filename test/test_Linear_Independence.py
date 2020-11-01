import unittest
# from utilities import getPath,parseNumber,update_json
from module.Vectors import Vectors


class TDD_LINEAR_INDEPENDENCE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1

    def test_Linear_Independence(self):
        v = Vectors()
        edge = round(v.get_third_edge(374, 506, 180-45*2))
        self.assertEqual(edge, 752)


if __name__ == '__main__':
    unittest.main()
