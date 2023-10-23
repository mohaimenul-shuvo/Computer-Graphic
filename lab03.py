from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()






def drawpoint(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()




def drawcircle(h,k,r):
    points=[]
    x=0
    y=r
    points.append((x, y))
    d=1-r
    while x<y:
        se = (2*x)-(2*y)+5
        e = (2*x)+3
        if d<0:


            d=d+e
            x+=1


        else:
            d = d + se
            x += 1
            y -= 1


        points.append((x,y)) # points contains all the pixels of zone 0
    return h,k,points
    drawzones(h,k,points)


def drawzones(h,k,points):
    for i in points:
        x=-i[0]
        y=-i[1]
        drawpoint(x + h, y + k)
    for i in points:
        x = i[0]
        y = -i[1]
        drawpoint(x + h, y + k)
    for i in points:
        x=i[1]
        y=-i[0]
        drawpoint(x + h, y + k)
    for i in points:
        x=i[0]
        y=i[1]
        drawpoint(x+h,y+k)


    for i in points:
        x=-i[1]
        y=i[0]
        drawpoint(x + h, y + k)
    for i in points:
        x=-i[1]
        y=-i[0]
        drawpoint(x + h, y + k)


    for i in points:
        x=i[1]
        y=i[0]
        drawpoint(x+h,y+k)
    for i in points:
        x=-i[0]
        y=i[1]
        drawpoint(x+h,y+k)








def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    h,k,point=drawcircle(250,250,250)
    drawzones(h,k,point)


    h,k,point=drawcircle(125, 250, 125)
    drawzones(h, k, point)
    h,k,point=drawcircle(375, 250, 125)
    drawzones(h, k, point)
    h,k,point=drawcircle(250, 375, 125)
    drawzones(h, k, point)
    h,k,point=drawcircle(250, 125, 125)
    drawzones(h, k, point)
    h,k,point=drawcircle(312.5, 141.8, 125)
    drawzones(h, k, point)
    h,k,point=drawcircle(312.5,358.3, 125)
    drawzones(h, k, point)
    h,k,point=drawcircle(187.5, 141.8, 125)
    drawzones(h, k, point)
    h,k,point=drawcircle(187.5, 358.3, 125)
    drawzones(h, k, point)


    glutSwapBuffers()






glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"19201095_Lab 3")
glutDisplayFunc(showScreen)


glutMainLoop()






