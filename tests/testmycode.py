from models.geometrics import Triangle
from models.matrix import Matrix
from utils.transformacoes import translate, transladar

tx = 9
ty = -5

T = Matrix(3,3,[1,0,tx,0,1,ty,0,0,1])

PA =  Matrix(3,1,[1,2,1])
PB =  Matrix(3,1,[1,-2,1])

res = T.dot(PA)

print(res)

res = T.dot(PB)

print(res)

edges = (
    (2, 0, 0),
    (1, 2, 0),
    (0, 1, 0)
)

triangle = Triangle(edges)

print(transladar(9,-5,0,triangle.edges))
