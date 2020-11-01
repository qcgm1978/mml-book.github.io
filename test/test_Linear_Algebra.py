from .Linear_Algebra import Linear_Algebra
import unittest
import numpy
np = numpy
# from utilities import getPath,parseNumber,update_json


class TDD_LINEAR_ALGEBRA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.foo = 1
        cls.l = Linear_Algebra()

    def test_Linear_Algebra(self):
        l = self.l
        self.assertIsInstance(l.vectors['objects']['Audio signals'], float)
        self.assertIsInstance(l.vectors['objects']['Rn'], tuple)

    def test_Systems_Linear_Equations(self):
        l = self.l
        self.assertRaises(numpy.linalg.LinAlgError, l.linalgSolve, [
                          [1, 1, 1], [1, -1, 2], [2, 0, 3]], [3, 2, 1])
        s = l.linalgSolve([[1, 1, 1], [1, -1, 2], [0, 1, 1]], [3, 2, 2])
        self.assertEqual(s.tolist(), [1, 1, 1])
        self.assertRaises(numpy.linalg.LinAlgError, l.linalgSolve, [
                          [1, 1, 1], [1, -1, 2], [2, 0, 3]], [3, 2, 5])
        s = l.lstsq([[1, 1, 1], [1, -1, 2], [2, 0, 3]], [3, 2, 5])
        Least_squares = s[0].astype(int)
        self.assertEqual(Least_squares.tolist(), [1, 1, 1])
        s = l.lstsq([[4, 4], [2, -4]], [5, 1])[0].round(2)
        self.assertEqual(s.tolist(), [1, 1 / 4])

    def test_Matrics(self):
        A = [[1, 2, 3], [3, 2, 1]]
        B = [[0, 2], [1, -1], [0, 1]]
        d = numpy.dot(A, B)
        d1 = numpy.dot(B, A)
        self.assertEqual(d.tolist(), [[2, 3], [2, 5]])
        self.assertEqual(d1.tolist(), [[6, 4, 2], [-2, 0, 2], [3, 2, 1]])
        self.assertNotEqual(d.tolist(), d1.tolist())
        A = np.matrix([[1, 2, 1], [4, 4, 5], [6, 7, 7]])
        B = np.matrix([[-7, -7, 6], [2, 1, -1], [4, 5, -4]])
        self.assertTrue((A*B).tolist() == (B*A).tolist()
                        == np.eye(A.shape[0]).tolist())

    def test_distributivity(self):
        C = np.matrix([[1, 2], [3, 4]])
        lam = 2
        phi = 3
        np.dot((lam+phi), C)
        temp0 = np.dot(phi, C)
        temp1 = np.dot(lam, C)
        self.assertEqual((temp0 + temp1).tolist(),
                         np.dot(phi + lam, C).tolist())

    def test_Gaussian_Elimination(self):
        A = np.matrix([[1, 0, 8, -4], [0, 1, 2, 12]])
        sol = np.vstack([42, 8])
        self.assertFalse(~(sol-[42, 8]).any())
        self.assertFalse(not np.any(sol-[42, 8]))
        self.assertTrue(np.all(sol-[42, 8]) == 0)
        f_o = np.vstack([42, 8, 0, 0])
        self.assertTrue(np.all(f_o-[[42], [8], [0], [0]]) == 0)
        self.assertTrue(all(np.dot(A, f_o) - [[42], [8]] == 0))
        self.assertEqual(f_o.shape, (4, 1))
        # Here column three is composed of col 1 and 2, and 3 is inverted.
        lam = 51345  # arbitrary scalar used to show the infinity of solutions.
        self.assertEqual(
            np.dot(A, lam*np.vstack([A[:, 2], -1, 0])) .tolist(), [[0], [0]])
        # Here column four is composed of col 1 and 2, and 4 is inverted.
        self.assertEqual(
            np.dot(A, lam * np.vstack([A[:, 3], 0, -1])).tolist(), [[0], [0]])
        self.assertEqual((np.dot(A, f_o) + np.dot(A, lam*np.vstack(
            [A[:, 2], -1, 0])) + np.dot(A, lam*np.vstack([A[:, 3], 0, -1]))).tolist(), [[42], [8]])
        a = 50  # for any arbitrary value a in R
        l_4 = [
            [-2, 4, -2, -1, 4],
            [4, -8, 3, -3, 1],
            [1, -2, 1, -1, 1],
            [1, -2, 0, -3, 4]
        ]
        A = np.vstack(l_4)
        l = [-3, 2, 0, a]
        b = np.vstack(l)
        Ab = np.hstack([A, b])
        self.assertEqual((Ab[:, -1]).tolist(), l)
        # Exchange of two equations. I.e. swap row 0 and 2.
        Ab[[0, 2]] = Ab[[2, 0]]
        # Addition of two equation, or rows. Subtract row 0 from 3.
        Ab[3] -= Ab[0]
        # Addition of two equation, or rows. Add 2 * row 0 to row 2.
        Ab[2] += 2 * Ab[0]
        # Addition of two equation, or rows. Subtract 4 * row 0 to row 1
        Ab[1] -= 4*Ab[0]
        # Addition of two equation, or rows. Add -Row 1 - Row 2
        Ab[3] += -Ab[1] - Ab[2]
        temp = (Ab[1]).copy()
        # Multiplication of an equation, or row, with a constant. Invert row 1
        Ab[1] *= -1
        self.assertEqual((Ab[1]).tolist(), np.negative(temp).tolist())
        Ab = Ab.astype(float)
        # Multiplication of an equation, or row, with a constant. Divide row 2 by -1/3
        Ab[2] *= -1/3
        Ab[:, 5][3] -= a + 1
        self.assertEqual(Ab[3].tolist(), np.zeros(6).tolist())
        self.assertEqual(A.tolist(), l_4)
        self.assertEqual(A.tolist(), np.mat(l_4).tolist())
        self.assertEqual(A.tolist(), np.array(l_4).tolist())
    def test_REF(self):
        s='''1 􀀀2 1 􀀀1 1 0
0 0 1 􀀀1 3 􀀀2
0 0 0 1 􀀀2 1
0 0 0 0 0 a + 1 '''
        m = self.l.convert_s(s)
        self.assertEqual(m, [[1, -2, 1, -1, 1, 0], [0, 0, 1, -1, 3, -2], [0, 0, 0, 1, -2, 1], [0, 0, 0, 0, 0, 'a+1']])
        self.assertTrue(self.l.is_REF(s,is_augumented=True))
        sol, lat = self.l.get_solutions(s, is_augumented=True)
        s='''􀀀2 4 􀀀2 􀀀1 4 􀀀3
4 􀀀8 3 􀀀3 1 2
1 􀀀2 1 􀀀1 1 0
1 􀀀2 0 􀀀3 4 a'''
        self.assertFalse(self.l.is_REF(s,is_augumented=True))
        print(sol)
        # self.assertEqual(sol, [[2,0,-1,1,0],[[2,1,0,0,0],[2,0,-1,2,1]]])

    def test_vstack(self):
        np = numpy
        A = np.array([1, 2, 3])
        B = np.array([2, 3, 4])
        self.assertEqual(np.vstack((A, B)).tolist(), np.array(
            [A, B]).tolist(), [[1, 2, 3], [2, 3, 4]])
        A = np.array([[1], [2], [3]])
        B = np.array([[2], [3], [4]])
        self.assertEqual(np.vstack((A, B)).tolist(), np.array(
            [*A, *B]).tolist(), [[1], [2], [3], [2], [3], [4]])
        A = [1.2, 1.2, 1.2, 1.2]
        self.assertEqual(np.vstack(A).tolist(),
                         np.array(A).reshape(4, 1).tolist())
        A = np.vstack(A)
        B = np.vstack([2, 2, 2, 2])
        hAB = np.hstack([A, B])
        vAB = np.vstack([A, B])
        self.assertEqual(hAB.tolist(), np.array([A, B]).T.tolist()[0])
        self.assertEqual(vAB.tolist(), np.array([A, B]).reshape(8, 1).tolist())

    def test_einsum(self):
        np = numpy
        a = np.arange(25).reshape(5, 5)
        b = np.arange(5)
        c = np.arange(6).reshape(2, 3)
        l = [it for index, item in enumerate(
            a) for ind, it in enumerate(item) if ind == index]
        self.assertEqual(l, [0, 6, 12, 18, 24])
        # Repeated subscript labels in one operand take the diagonal. For example, np.einsum('ii', a) is equivalent to np.trace(a).
        ein = np.einsum('ii', a)
        self.assertTrue(np.einsum(a, [0, 0]) ==
                        ein == sum(l) == np.trace(a) == 60)
        A = np.vstack([1.2, 1.2, 1.2, 1.2])
        B = np.vstack([2, 2, 2, 2])
        # In implicit mode, the chosen subscripts are important since the axes of the output are reordered alphabetically. This means that np.einsum('ij', a) doesn’t affect a 2D array, while np.einsum('ji', a) takes its transpose. Additionally, np.einsum('ij,jk', a, b) returns a matrix multiplication, while, np.einsum('ij,jh', a, b) returns the transpose of the multiplication since subscript ‘h’ precedes subscript ‘i’.
        C = np.einsum('il,lj', A, B)
        transpose_mul = np.dot(A.T, B)*np.ones(np.shape(A)).tolist()
        self.assertTrue((C).tolist() == transpose_mul.tolist() ==
                        [[9.6], [9.6], [9.6], [9.6]])

    def test_echelon(self):
        l = self.l
        m = np.mat([[1, -2, 1, -1, 1],
                    [0, 0, 1, -1, 3],
                    [0, 0, 0, 1, -2],
                    [0, 0, 0, 0, 0]])
        self.assertTrue(l.is_REF(m))
        self.assertEqual(l.get_Basic_Free(m)[0], ['x1', 'x3', 'x4'])
        self.assertEqual(l.get_Basic_Free(m)[1], ['x2', 'x5'])

        A = [[1, 3, 0, 0, 3],
             [0, 0, 1, 0, 9],
             [0, 0, 0, 1, -4]]
        self.assertEqual(l.get_Basic_Free(A)[0], ['x1', 'x3', 'x4'])
        self.assertEqual(l.get_Basic_Free(A)[1], ['x2', 'x5'])
        self.assertTrue(l.is_reduced_echelon(A))
        sol, latex = l.get_solutions(A)
        self.assertEqual(sol.tolist(), np.vstack(
            [[3, -1, 0, 0, 0], [3, 0, 9, -4, -1]]).tolist())
        self.assertEqual(
            latex, r'''$\left\{\boldsymbol{x} \in \mathbb{R}^{5}: \boldsymbol{x}=\lambda_{1}\left[\begin{array}{c}3 \\ -1 \\ 0 \\ 0 \\ 0\end{array}\right]+\lambda_{2}\left[\begin{array}{c}3 \\ 0 \\ 9 \\ -4 \\ -1\end{array}\right], \quad \lambda_{1}, \lambda_{2} \in \mathbb{R}\right\}$''')


if __name__ == '__main__':
    unittest.main()
