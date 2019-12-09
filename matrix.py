import math
from abstracts.abstract_matrix import AbstractMatrix


class Matrix(AbstractMatrix):
    """
            This class was used to represent a matrix
            by:Bárbara Perina
        """

    MSG_DIFFERENT_SIZES = "The matrixs doesn't have the same size"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        i, j = key
        return self.data[(j - 1) + (i - 1) * self.cols]

    def __setitem__(self, key, value):
        try:
            i, j = key
            self.data[(j - 1) + (i - 1) * self.cols] = value
        except:
            print(Exception, " occurred")

    def __repr__(self):
        return str(self)

    def __str__(self):
        matrix = "";
        for row in range(1,self.rows+1):
            for col in range(1,self.cols+1):
                # matrix = matrix + "(row:" + str(row+1) + " column:" + str(col+1) + "): "
                matrix = matrix + str(self[row,col]) + "\t"
            matrix = matrix + "\n"
        return matrix

    # other + matrix
    def __radd__(self, other):
        return self + other

    # matrix + other
    def __add__(self, other):
        res = Matrix(self.rows, self.cols)
        if(type(other) == Matrix):
            # print("Add self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return  "error __add__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] + other[i, j]
        else:
            # print("Add self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] + other
        return res

    # other - matrix
    def __rsub__(self, other):
        return self - other

    # matrix - other
    def __sub__(self, other):
        res = Matrix(self.rows, self.cols)
        if(type(other) == Matrix):
            # print("Sub self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return "error __sub__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] - other[i, j]
        else:
            # print("Sub self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] - other
        return res

    # other * matrix
    def __rmul__(self, other):
        return self * other

    # matriz * other
    def __mul__(self, other):
        res = Matrix(self.rows, self.cols)
        if (type(other) == Matrix):
            # print("Mul self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return "error __mul__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] * other[i, j]
        else:
            # print("Mul self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] * other
        return res

    # other / matriz
    def __rtruediv__(self, other):
        return self / other
    # matriz / other
    def __truediv__(self, other):
        res = Matrix(self.rows, self.cols)
        if (type(other) == Matrix):
            # print("Truediv self.matrix with: \n" + str(other))
            if self.rows != other.rows or self.cols != other.cols:
                print(self.MSG_DIFFERENT_SIZES)
                return "error __truediv__ matrix"
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] / other[i, j]
        else:
            # print("Truediv self.matrix with a scale number: " + other)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i, j] = self[i, j] / other
        return res

    # self * other
    def dot(self, other):
        if(type(other) == Matrix):
            if(self.cols != other.rows):
                return "matrix A must be the same amount of columns as amount matrix B rows amount"
            res = Matrix(self.rows, other.cols)
            for col in range(1, self.cols + 1):
                for row in range(1, self.rows + 1):
                    for othercol in range(1, other.cols + 1):
                        res[row, othercol] += self[row, col] * other[col, othercol]
            return res
        else:
            return "the dot method only works between matrixs"

    # other * self
    def rdot(self, other):
        if(type(other) == Matrix):
            if(self.rows != other.cols):
                return "matrix A must be the same amount of columns as amount matrix B rows amount"
            res = Matrix(self.rows, other.cols)
            for col in range(1, other.cols + 1):
                for row in range(1, other.rows + 1):
                    for selfcol in range(1, self.cols + 1):
                        res[row, selfcol] += other[row, col] * self[col, selfcol]
            return res
        else:
            return "the dot method only works between matrixs"

    def transpose(self):
        res = Matrix(self.cols, self.rows)

        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                res[j, i] = self[i, j]

        return res

    def gauss_jordan(self):
        """Aplica o algoritmo de Gauss Jordan na matriz

        Aplica o método de Gauss-Jordan na matriz corrente. Pode ser utilizado para resolver
        um sistema de equações lineares, calcular matrix inversa, etc.

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(3,4,[1, -2, 1, 0, 0, 2, -8, 8, 5, 0, -5, 10])
            #> a
                1.0000   -2.0000   1.0000   0.0000
                0.0000    2.0000  -8.0000   8.0000
                5.0000    0.0000  -5.0000   10.0000
            #> c = a.gauss_jordan()
            #> c
                1.0000    0.0000   0.0000   1.0000
                0.0000    1.0000   0.0000   0.0000
                0.0000    0.0000   1.0000  -1.0000
        """
        pass

    def inverse(self):
        """Calcula a matriz inversa da matriz corrente

        Realiza o calculo da matrix inversa utilizando o algoritmo de Gauss-Jordan.

        "Returns:
            Retorna a matrix resultante da operação, por exemplo:

            #> a = Matrix(2,2,[1, 2, 3, 4])
            #> a
                1.0000   -2.0000   1.0000   0.0000
                0.0000    2.0000  -8.0000   8.0000
                5.0000    0.0000  -5.0000   10.0000
            #> c = a.inverse()
            #> c
                -2.0000   1.0000
                1.5000   -0.5000

        """
        pass

    def float_format(self):
        res = Matrix(self.rows, self.cols)
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                res[i, j] = float("{0:.2f}".format(self[i, j]))
        return res

    def normalized (self):
        vector = self.data
        soma = 0
        for v in vector:
            square = v*v
            soma+=square
        res = math.sqrt(soma)
        return res

    def module(self, eigenvector):
        # print(eigenvector)
        module = 0
        for d in eigenvector.data:
            module = module + (d*d)
        module = math.sqrt(module)
        return module

    def get_matrix_bigger_element(self):
        bigger = self.data[0]
        for element in self.data:
            if element > bigger:
                bigger = element
        return bigger

    def eigen(self):
        # print('matriz: \n' + str(self))
        # result = self.power_method()
        # eigenvalue = result[0]
        # eigenvector = result[1]
        # print('eigenvalue: \n' + str(eigenvalue))
        # print('eigenvector: \n' + str(eigenvector))

        A = self
        eigenvalues = []
        eigenvectors = []
        for x in range(0,3):
            B = A.power_method()
            eigenvalue = B[0]
            eigenvector = B[1]
            eigenvalues.append(B[0])
            eigenvectors.append(B[1])
            print('eigenvalue: \n' + str(eigenvalue))
            print('eigenvector: \n' + str(eigenvector))
            A = A.deflation(eigenvalue, eigenvector)


        # B = self.deflation(eigenvalue,eigenvector)
        # print('B: \n' + str(B))
        #
        # result = B.power_method()
        # eigenvalue = result[0]
        # eigenvector = result[1]
        # print('eigenvalue: \n' + str(eigenvalue))
        # print('eigenvector: \n' + str(eigenvector))
        #
        # B2 = B.deflation(eigenvalue, eigenvector)
        # print('B: \n' + str(B))
        #
        # result = B2.power_method()
        # eigenvalue = result[0]
        # eigenvector = result[1]
        # print('eigenvalue: \n' + str(eigenvalue))
        # print('eigenvector: \n' + str(eigenvector))

        return  eigenvalues, eigenvectors

    def power_method(self):
        MAX_ITERATIONS = 9
        MATRIX_SIZE = self.rows
        ITERATION = 1

        data = [1] * (MATRIX_SIZE * 1)
        matriz_inicial = Matrix(MATRIX_SIZE, 1, data)

        while ITERATION <= MAX_ITERATIONS:
            # print('ITERAÇÃO ' + str(ITERATION))
            # print('A= \n'+ str(self))
            # print('\nx= \n' + str(matriz_inicial))
            x = self.dot(matriz_inicial)
            x = (1/x.get_matrix_bigger_element()) * x
            # print('x'+str(ITERATION)+'= ' + str(x))
            matriz_inicial = x
            ITERATION += 1
        x = self.dot(matriz_inicial)

        #get eigenvalue
        eigenvalue = x.get_matrix_bigger_element()
        eigenvalue = float("{0:.2f}".format(eigenvalue))
        # print('eigenvalue= ' + str(eigenvalue))

        #get eigenvector
        eigenvector = (1 / x.get_matrix_bigger_element()) * x
        eigenvector = eigenvector.float_format()
        # print('eigenvector= \n' + str(eigenvector))

        return eigenvalue, eigenvector

    def deflation(self, eigenvalue, eigenvector):
        module = self.module(eigenvector)
        # print(module)
        eigenvector = eigenvector/module
        result = eigenvalue*(eigenvector.dot(eigenvector.transpose()))
        B = self - result
        return B

    def pagerank(self):
        # r(t+1) = h r(t)
        data = [1/self.rows] * (self.rows * 1)
        matriz_inicial = Matrix(self.rows, 1, data)

        result = self.dot(matriz_inicial)
        print(result)
        pass