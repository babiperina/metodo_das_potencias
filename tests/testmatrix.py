import unittest
from matrix import Matrix

class TestMatrixMethods(unittest.TestCase):

    def test_getitem(self):
        a = Matrix(2, 2, [1, 2, 3, 4])
        self.assertEqual(a[1,2], 2, 'Indexação está incorreta')

    @unittest.expectedFailure
    def test_getitem_failure(self):
        a = Matrix(2, 2, [1, 2, 3, 4])
        with self.assertRaises(Exception): a[3,3]

    def test_setitem(self):
        a = Matrix(2, 2, [1, 2, 3, 4])
        a[2,2] = 100
        self.assertEqual(a[2,2], 100, 'Indexação está incorreta')

    @unittest.expectedFailure
    def test_setitem_failure(self):
        a = Matrix(2, 2, [1, 2, 3, 4])
        with self.assertRaises(Exception): a[3,3] = 5

    def test_radd(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c =  b + a
        self.assertEqual(c[2,2], 55, 'A operação de soma não esta consistente')

        c = 2 + a
        self.assertEqual(c[2,2], 7, 'A operação de soma não esta consistente')


    def test_add(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c =  a + b
        self.assertEqual(c[2,2], 55, 'A operação de soma não esta consistente')

        c = 2 + a
        self.assertEqual(c[2,2], 7, 'A operação de soma não esta consistente')

    @unittest.expectedFailure
    def test_add_failure(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(2, 2, [10, 20, 30, 40])

        c =  a + b
        self.assertEqual(c[2,2], 55, 'A operação de soma não esta consistente')

        c = 2 + a
        self.assertEqual(c[2,2], 7, 'A operação de soma não esta consistente')

    def test_rsub(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c = b - a
        self.assertEqual(c[2,2], 45, 'A operação de subtração não esta consistente')

        c = 2 - a
        self.assertEqual(c[2,2], 3, 'A operação de subtração não esta consistente')

    def test_sub(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c =  a - b
        self.assertEqual(c[2,2], -45, 'A operação de subtração não esta consistente')

        c = a - 2
        self.assertEqual(c[2,2], 3, 'A operação de subtração não esta consistente')

    @unittest.expectedFailure
    def test_sub_failure(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(2, 2, [10, 20, 30, 40])

        c =  a - b
        self.assertEqual(c[2,2], -45, 'A operação de subtração não esta consistente')

        c = a - 2
        self.assertEqual(c[2,2], 3, 'A operação de subtração não esta consistente')

    def test_rmul(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c = b * a
        self.assertEqual(c[2,2], 250, 'A operação de multiplicação não esta consistente')

        c = 2 * a
        self.assertEqual(c[2,2], 10, 'A operação de multiplicação não esta consistente')

    def test_mul(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c = a * b
        self.assertEqual(c[2,2], 250, 'A operação de multiplicação não esta consistente')

        c = a * 2
        self.assertEqual(c[2,2], 10, 'A operação de multiplicação não esta consistente')

    @unittest.expectedFailure
    def test_mul(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(2, 2, [10, 20, 30, 40])

        c = a * b
        self.assertEqual(c[2,2], 250, 'A operação de multiplicação não esta consistente')

        c = a * 2
        self.assertEqual(c[2,2], 10, 'A operação de multiplicação não esta consistente')

    def test_rtruediv(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c = b / a
        self.assertEqual(c[2,2], 10, 'A operação de divisão não esta consistente')

        c = 2 / a
        self.assertEqual(c[2,2], 2.5, 'A operação de divisão não esta consistente')

    def test_truediv(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(3, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90])

        c = a / b
        self.assertEqual(c[2,2], 0.1, 'A operação de divisão não esta consistente')

        c = a / 2
        self.assertEqual(c[2,2], 2.5, 'A operação de divisão não esta consistente')

    @unittest.expectedFailure
    def test_truediv_failure(self):
        a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        b = Matrix(2, 2, [10, 20, 30, 40])

        c = a / b
        self.assertEqual(c[2,2], 0.1, 'A operação de divisão não esta consistente')

        c = a / 2
        self.assertEqual(c[2,2], 2.5, 'A operação de divisão não esta consistente')

    def test_dot(self):
        a = Matrix(10, 10, [26, 70, 63,  6,  1, 53, 20, 24, 50, 31, 61, 18, 26, 13, 58, 97, 36,
                            58,  6, 82,  6, 86,  0, 27, 82, 83, 83, 52, 28, 47, 50, 37, 98, 83,
                            51, 23, 39, 22, 77, 64, 59, 40, 66, 73, 24, 18, 99,  8, 22, 71, 48,
                            10, 11, 80, 45, 46, 41, 33,  0, 13, 73, 56, 59,  9, 47, 80, 68, 15,
                            48, 23, 23,  7, 51, 53, 65, 44, 13, 39, 95, 52, 32, 19,  3, 97, 86,
                            32, 72, 40, 27,  8, 28,  2, 99, 69, 21,  6, 12, 52, 74, 62])
        b = Matrix(10, 20, [73, 94, 57, 13, 31, 77, 12, 85, 26,  9, 27, 15,  4, 73, 59, 33, 53,
                            74, 35, 17, 14, 96, 27,  8, 50, 14, 71,  5, 99,  2, 49, 23, 53, 95,
                            18, 58,  4, 56, 78,  9, 44, 21, 55, 11, 75, 41, 79, 77, 97, 98, 37,
                            22, 97, 57, 23, 23, 63, 34, 88, 90, 25, 37, 27, 35, 97, 59,  6, 78,
                            50, 40, 48, 94, 73, 20, 62, 76, 74,  8,  3, 77, 46, 43, 89, 12, 47,
                            68, 95, 41, 68, 71, 98, 87, 95, 77, 34, 73, 53, 21, 40, 21, 28, 44,
                            3, 15, 36, 17, 64, 97, 11, 51, 53, 18, 33, 93, 65, 65, 34, 87, 19,
                            58, 25, 99, 38, 55, 24,  9, 84, 19, 17, 82,  2, 96, 55, 53, 29, 36,
                            47,  3, 79, 63, 74,  7, 89, 62, 37, 97, 18,  2, 32, 45, 74,  3, 96,
                            0, 78, 68, 21, 16, 79, 79, 25, 17, 11, 74, 13, 76, 80, 57, 22,  4,
                            89, 17, 81, 55, 68, 59, 95, 18,  6, 10, 29,  6, 27, 64, 51, 21, 42,
                            64, 48, 54, 51, 57, 68, 29, 36, 74, 92, 74, 82, 78])

        c = a.dot(b)
        self.assertEqual(c.rows, a.rows, 'Matriz resultante inconsistente')
        self.assertEqual(c.cols, b.cols, 'Matriz resultante inconsistente')
        self.assertEqual(c[7, 17], 23874, 'Multiplicação de matrizes inconsistente')

    @unittest.expectedFailure
    def test_dot_failure(self):
        a = Matrix(10, 10, [26, 70, 63,  6,  1, 53, 20, 24, 50, 31, 61, 18, 26, 13, 58, 97, 36,
                            58,  6, 82,  6, 86,  0, 27, 82, 83, 83, 52, 28, 47, 50, 37, 98, 83,
                            51, 23, 39, 22, 77, 64, 59, 40, 66, 73, 24, 18, 99,  8, 22, 71, 48,
                            10, 11, 80, 45, 46, 41, 33,  0, 13, 73, 56, 59,  9, 47, 80, 68, 15,
                            48, 23, 23,  7, 51, 53, 65, 44, 13, 39, 95, 52, 32, 19,  3, 97, 86,
                            32, 72, 40, 27,  8, 28,  2, 99, 69, 21,  6, 12, 52, 74, 62])
        b = Matrix(10, 20, [73, 94, 57, 13, 31, 77, 12, 85, 26,  9, 27, 15,  4, 73, 59, 33, 53,
                            74, 35, 17, 14, 96, 27,  8, 50, 14, 71,  5, 99,  2, 49, 23, 53, 95,
                            18, 58,  4, 56, 78,  9, 44, 21, 55, 11, 75, 41, 79, 77, 97, 98, 37,
                            22, 97, 57, 23, 23, 63, 34, 88, 90, 25, 37, 27, 35, 97, 59,  6, 78,
                            50, 40, 48, 94, 73, 20, 62, 76, 74,  8,  3, 77, 46, 43, 89, 12, 47,
                            68, 95, 41, 68, 71, 98, 87, 95, 77, 34, 73, 53, 21, 40, 21, 28, 44,
                            3, 15, 36, 17, 64, 97, 11, 51, 53, 18, 33, 93, 65, 65, 34, 87, 19,
                            58, 25, 99, 38, 55, 24,  9, 84, 19, 17, 82,  2, 96, 55, 53, 29, 36,
                            47,  3, 79, 63, 74,  7, 89, 62, 37, 97, 18,  2, 32, 45, 74,  3, 96,
                            0, 78, 68, 21, 16, 79, 79, 25, 17, 11, 74, 13, 76, 80, 57, 22,  4,
                            89, 17, 81, 55, 68, 59, 95, 18,  6, 10, 29,  6, 27, 64, 51, 21, 42,
                            64, 48, 54, 51, 57, 68, 29, 36, 74, 92, 74, 82, 78])

        c = b.dot(a)
        self.assertEqual(c.rows, a.rows, 'Matriz resultante inconsistente')
        self.assertEqual(c.cols, b.cols, 'Matriz resultante inconsistente')
        self.assertEqual(c[7, 17], 23874, 'Multiplicação de matrizes inconsistente')

    def test_transpose(self):
        a = Matrix(10, 20, [73, 94, 57, 13, 31, 77, 12, 85, 26,  9, 27, 15,  4, 73, 59, 33, 53,
                            74, 35, 17, 14, 96, 27,  8, 50, 14, 71,  5, 99,  2, 49, 23, 53, 95,
                            18, 58,  4, 56, 78,  9, 44, 21, 55, 11, 75, 41, 79, 77, 97, 98, 37,
                            22, 97, 57, 23, 23, 63, 34, 88, 90, 25, 37, 27, 35, 97, 59,  6, 78,
                            50, 40, 48, 94, 73, 20, 62, 76, 74,  8,  3, 77, 46, 43, 89, 12, 47,
                            68, 95, 41, 68, 71, 98, 87, 95, 77, 34, 73, 53, 21, 40, 21, 28, 44,
                            3, 15, 36, 17, 64, 97, 11, 51, 53, 18, 33, 93, 65, 65, 34, 87, 19,
                            58, 25, 99, 38, 55, 24,  9, 84, 19, 17, 82,  2, 96, 55, 53, 29, 36,
                            47,  3, 79, 63, 74,  7, 89, 62, 37, 97, 18,  2, 32, 45, 74,  3, 96,
                            0, 78, 68, 21, 16, 79, 79, 25, 17, 11, 74, 13, 76, 80, 57, 22,  4,
                            89, 17, 81, 55, 68, 59, 95, 18,  6, 10, 29,  6, 27, 64, 51, 21, 42,
                            64, 48, 54, 51, 57, 68, 29, 36, 74, 92, 74, 82, 78])

        c = a.transpose()
        self.assertEqual(c.rows, a.cols, 'Matriz resultante inconsistente')
        self.assertEqual(c.cols, a.rows, 'Matriz resultante inconsistente')
        self.assertEqual(c[17, 7], a[7, 17], 'Multiplicação de matrizes inconsistente')

    def test_gauss_jordan(self):
        a = Matrix(3, 4, [3, 2, -1, 1, 2, -2, 4, -2, -1, 0.5, -1, 0])
        c = a.gauss_jordan()
        self.assertEqual(c[1,1], 1, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertEqual(c[2,2], 1, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertEqual(c[3,3], 1, 'Erro ao calcular o método de Gauss-Jordan')

        self.assertEqual(c[1,2], 0, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertEqual(c[1,3], 0, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertEqual(c[2,1], 0, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertEqual(c[2,3], 0, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertEqual(c[3,1], 0, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertEqual(c[3,2], 0, 'Erro ao calcular o método de Gauss-Jordan')

        self.assertAlmostEqual(c[1,4], 1, 10,'Erro ao calcular o método de Gauss-Jordan')
        self.assertAlmostEqual(c[2,4], -2, 10, 'Erro ao calcular o método de Gauss-Jordan')
        self.assertAlmostEqual(c[3,4], -2, 10, 'Erro ao calcular o método de Gauss-Jordan')

    def test_norm(self):
        a = Matrix(2,1,[-9,12])
        self.assertEqual(a.norm(), 15, 'Erro ao calcular a norma')

    def test_power_method(self):
        a = Matrix(3, 3, [6, -2, 2, -2, 3, -1, 2, -1, 3])
        result = a.power_method()
        eigenvalue = result[0]
        eigenvector = result[1]
        self.assertEqual(eigenvalue, 7.9998, 'Erro ao calcular o auto-valor')
        self.assertEqual(eigenvector[1,1], 1.0, 'Erro ao calcular o auto-vetor')
        self.assertEqual(eigenvector[1,2], -0.5, 'Erro ao calcular o auto-vetor')
        self.assertEqual(eigenvector[1,3], 0.5, 'Erro ao calcular o auto-vetor')

    def test_eigen(self):
        pass

if __name__ == "__main__":
    unittest.main()