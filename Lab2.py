import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 700, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 700, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#======================================================================================================

def mid_point_line(x0, y0, x1, y1):
    zone = 0
    dx = x1 - x0
    dy = y1 - y0
    #print(f"previous: {dx}, {dy}")
    if dx >= 0 and dy >= 0 and abs(dy) > abs(dx):
        zone = 1
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    dx = x1 - x0
    dy = y1 - y0
    #print(f"After: {dx}, {dy}")

    d_init = 2*dy - dx

    x, y = x0, y0
    print(x, y)
    if zone == 1:
        draw_points(y, x)   #convert to zone 0
    else:
        draw_points(x, y)


    while(x <= x1 and y <= y1):
        if d_init > 0:
            x = x+1
            y = y+1
            d_init += (2*dy - dx)
        else:
            x = x+1
            d_init += (2*dy)

        if zone == 1:
            draw_points(y, x)  #convert to zone 0
        else:
            draw_points(x, y)

def draw_id():
    id = "19201095"
    a = id[-2]
    b = id[-1]

    ######################### For a #############################
    if a == '0':
        #mid_point_line(x0,y0,x1,y1)
        mid_point_line(100, 50, 100, 450)
        mid_point_line(100, 450, 300, 450)
        mid_point_line(300, 50, 300, 450)
        mid_point_line(100, 50, 300, 50)

    elif a == '1':
        mid_point_line(300, 50, 300, 450)

        mid_point_line(250, 50, 350, 50)
        mid_point_line(250, 400, 300, 450)

    elif a == '2':
        mid_point_line(100, 450, 300, 450)
        mid_point_line(300, 250, 300, 450)
        mid_point_line(100, 250, 300, 250)
        mid_point_line(100, 50, 100, 250)
        mid_point_line(100, 50, 300, 50)

    elif a == '3':
        mid_point_line(100, 450, 300, 450)
        mid_point_line(300, 250, 300, 450)
        mid_point_line(100, 250, 300, 250)
        mid_point_line(300, 50, 300, 250)
        mid_point_line(100, 50, 300, 50)

    elif a == '4':
        mid_point_line(100, 250, 100, 450)
        mid_point_line(100, 250, 300, 250)
        mid_point_line(300, 250, 300, 450)
        mid_point_line(300, 50, 300, 250)


    elif a == '5':
        mid_point_line(100, 450, 300, 450)
        mid_point_line(100, 250, 100, 450)
        mid_point_line(100, 250, 300, 250)
        mid_point_line(300, 50, 300, 250)
        mid_point_line(100, 50, 300, 50)

    elif a == '6':
        mid_point_line(100, 450, 300, 450)
        mid_point_line(100, 250, 100, 450)
        mid_point_line(100, 250, 300, 250)
        mid_point_line(300, 50, 300, 250)
        mid_point_line(100, 50, 300, 50)
        mid_point_line(100, 50, 100, 250)

    elif a == '7':
        mid_point_line(100, 450, 300, 450)
        mid_point_line(300, 250, 300, 450)
        mid_point_line(300, 50, 300, 250)
        #mid_point_line(100, 50, 600, 450)

    elif a == '8':
        mid_point_line(100, 450, 300, 450)
        mid_point_line(300, 50, 300, 450)
        mid_point_line(100, 50, 300, 50)
        mid_point_line(100, 50, 100, 450)
        mid_point_line(100, 250, 300, 250)

    elif a == '9':
        mid_point_line(100, 450, 300, 450)
        mid_point_line(300, 50, 300, 450)
        mid_point_line(100, 50, 300, 50)
        mid_point_line(100, 250, 100, 450)
        mid_point_line(100, 250, 300, 250)




    ############## For b ###########################
    if b == '0':
        #mid_point_line(x0,y0,x1,y1)
        mid_point_line(400, 50, 400, 450)
        mid_point_line(400, 450, 600, 450)
        mid_point_line(600, 50, 600, 450)
        mid_point_line(400, 50, 600, 50)

    elif b == '1':
        mid_point_line(600, 50, 600, 450)

        mid_point_line(550, 50, 650, 50)
        mid_point_line(550, 400, 600, 450)

    elif b == '2':
        mid_point_line(400, 450, 600, 450)
        mid_point_line(600, 250, 600, 450)
        mid_point_line(400, 250, 600, 250)
        mid_point_line(400, 50, 400, 250)
        mid_point_line(400, 50, 600, 50)

    elif b == '3':
        mid_point_line(400, 450, 600, 450)
        mid_point_line(600, 250, 600, 450)
        mid_point_line(400, 250, 600, 250)
        mid_point_line(600, 50, 600, 250)
        mid_point_line(400, 50, 600, 50)

    elif b == '4':
        mid_point_line(400, 250, 400, 450)
        mid_point_line(400, 250, 600, 250)
        mid_point_line(600, 250, 600, 450)
        mid_point_line(600, 50, 600, 250)


    elif b == '5':
        mid_point_line(400, 450, 600, 450)
        mid_point_line(400, 250, 400, 450)
        mid_point_line(400, 250, 600, 250)
        mid_point_line(600, 50, 600, 250)
        mid_point_line(400, 50, 600, 50)

    elif b == '6':
        mid_point_line(400, 450, 600, 450)
        mid_point_line(400, 250, 400, 450)
        mid_point_line(400, 250, 600, 250)
        mid_point_line(600, 50, 600, 250)
        mid_point_line(400, 50, 600, 50)
        mid_point_line(400, 50, 400, 250)

    elif b == '7':
        mid_point_line(400, 450, 600, 450)
        mid_point_line(600, 250, 600, 450)
        mid_point_line(600, 50, 600, 250)
        #mid_point_line(100, 50, 600, 450)

    elif b == '8':
        mid_point_line(400, 450, 600, 450)
        mid_point_line(600, 50, 600, 450)
        mid_point_line(400, 50, 600, 50)
        mid_point_line(400, 50, 400, 450)
        mid_point_line(400, 250, 600, 250)

    elif b == '9':
        mid_point_line(400, 450, 600, 450)
        mid_point_line(600, 50, 600, 450)
        mid_point_line(400, 50, 600, 50)
        mid_point_line(400, 250, 400, 450)
        mid_point_line(400, 250, 600, 250)




#======================================================================================================

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0,1.0,0.0)  # konokichur color set (RGB)
    # call the draw methods here
    #draw_points(250, 250)
    draw_id()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()