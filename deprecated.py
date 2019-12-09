def get_matrix_smaller_element(self, matrix):
    smaller_element = matrix.data[0]
    for element in matrix.data:
        if element < smaller_element:
            smaller_element = element
    return smaller_element

def get_eigen_value(self, NORMALIZED_X):
    X = NORMALIZED_X.transpose();
    # Matrix(NORMALIZED_X.cols, NORMALIZED_X.rows, NORMALIZED_X.data);
    A = self.dot(NORMALIZED_X);
    A = A.transpose();
    adotx = A.dot(NORMALIZED_X)
    xdotx = X.dot(NORMALIZED_X)
    return adotx / xdotx

def get_eigen_vector(self, EIGENVALUE, NORMALIZED_X):
    # print(EIGENVALUE[1,1])
    # print(NORMALIZED_X)
    return EIGENVALUE[1 ,1] * NORMALIZED_X

# A = matrix nxn
def eigen(self):
    A = self
    print(A)
    # gera B
    # B = A - lambda/|v1| . v1 . v1T
    eigensA = self.power_method()
    # qtdeIteracoes n

    return eigensA

# v - autovetor que eu descobri
# v1 * v1T(transposta)
# lambda auto valor
# lambda/modulo auto vetor
# B = A - lambda/|v1| . v1 . v1T
def hotling_deflation(self):
    A = self
    eigenvalues = []
    eigenvectors = []
    pm = A.power_method()
    y = pm[0]
    v = pm[1]
    norm_v = v.norm();
    vT = v.transpose()
    print('lambda(autovalor): \n' + str(y))
    print('\nmodulo v: \n' + str(norm_v))
    print('\nv: \n' + str(v))
    print('vT: \n' + str(vT))
    y_norm_v = y/ norm_v
    print('lambda/norm_v: \n' + str(y_norm_v))
    v_vt = v.dot(vT)
    print('v * vT: \n' + str(v_vt))
    minus = y_norm_v * v_vt
    print('minus_part: \n' + str(minus))
    B = A - minus
    print('B: \n' + str(B))
    # B = A - y/norm_v * v * vT;
    print('\nA: \n' + str(A))
    # print(B)
    # gera B
    # B = A - y/norm_v . v . vT
    eigensA = B.power_method()
    # qtdeIteracoes n
    eigenvalues = eigensA[0]
    eigenvectors = eigensA[1]

    return eigenvalues, eigenvectors


def power_method(self):
    MAX_ITERATIONS = 7
    MATRIX_SIZE = self.rows
    ITERATION = 1

    data = [1] * (MATRIX_SIZE * 1)
    matriz_inicial = Matrix(MATRIX_SIZE, 1, data)

    while ITERATION <= MAX_ITERATIONS:
        X = self.dot(matriz_inicial)
        matriz_inicial = X
        menor_matriz = self.get_matrix_smaller_element(X)
        ITERATION += 1
    NORMALIZED_X = X / menor_matriz

    eigenvalue = self.get_eigen_value(NORMALIZED_X)
    eigenvector = self.get_eigen_vector(eigenvalue, NORMALIZED_X)
    eigenvalue = eigenvalue[1, 1]

    # return [eigenvalues[1, 1], [eigenvectors[1, 1], eigenvectors[1, 2], eigenvectors[1, 3]]]
    return eigenvalue, eigenvector