import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from utils.transformacoes import *

from models.geometrics import Triangle


def drawTriangle(triangle):
    glBegin(GL_LINES)
    for aresta in triangle.arestas:
        for vertex in aresta:
            glVertex3fv(triangle.edges[vertex])
    glEnd()

def main():
    edges = (
        (2, 0, 0),
        (1, 2, 0),
        (0, 1, 0)
    )

    triangle = Triangle(edges)

    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(150, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("CIMA")
                    glTranslatef(0,1,0)
                elif event.key == pygame.K_DOWN:
                    print("BAIXO")
                    glTranslatef(0,-1,0)
                elif event.key == pygame.K_LEFT:
                    print("ESQUERDA")
                    glTranslatef(-1,0,0)
                elif event.key == pygame.K_RIGHT:
                    print("DIREITA")
                    glTranslatef(1,0,0)
                elif event.key == pygame.K_q:
                    print("ZOOM IN")
                    glTranslatef(0, 0, 1)
                elif event.key == pygame.K_w:
                    print("ZOOM out")
                    glTranslatef(0, 0, -1)
                else:
                    print(event.key)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawTriangle(triangle)
        # rotate(90,1,triangle.edges)
        # glRotatef(1, 1, 0, 0)
        pygame.display.flip()
        pygame.time.wait(100)


main()
