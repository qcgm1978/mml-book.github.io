import unittest
from module.matrix.programiz import Matrix
class TDD_MATRIX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
    def test_matrix(self):
        A = [[1, 4, 5], 
    [-5, 8, 9]]
        self.assertIsInstance(A,list)
        Matrix()
        A = [[1, 4, 5, 12], 
            [-5, 8, 9, 0],
            [-6, 7, 11, 19]]

        self.assertEqual([-5, 8, 9, 0], A[1])      # 2nd row
        self.assertEqual(9, A[1][2])   # 3rd element of 2nd row
        self.assertEqual(12, A[0][-1])   # Last element of 1st Row

        column = []       # empty list
        for row in A:
            column.append(row[2])   

        self.assertEqual([5,9,11], column)
if __name__ == '__main__':
    unittest.main()
                