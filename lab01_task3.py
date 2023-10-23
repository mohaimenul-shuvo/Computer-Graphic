from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *




def draw_lines(x1,y1,x2,y2):
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)#jekhane show korbe pixel
    glEnd()




def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(1.0, 1.0, 0.0) # color set (RGB)
    #call the draw methods here
    #Drawing 1
    glColor3f(0.0, 1.0, 1.0)
    draw_lines(50,400,50,600)


    #Drawing 9
    glColor3f(1.0, 0.0, 1.0)
    draw_lines(70, 500, 70, 600)
    draw_lines(70, 600, 150, 600)
    draw_lines(150, 600, 150, 400)
    draw_lines(70, 400, 150, 400)
    draw_lines(70, 500, 150, 500)


    #Drawing 2
    glColor3f(1.0, 0.0, 0.0)
    draw_lines(170, 600, 250, 600)
    draw_lines(250, 600, 250, 500)
    draw_lines(170, 500, 250, 500)
    draw_lines(170, 500, 170, 400)
    draw_lines(170, 400, 250, 400)


    #Drawing 0
    glColor3f(0.5, 0.0, 1.0)
    draw_lines(270, 600, 350, 600)
    draw_lines(270, 600, 270, 400)
    draw_lines(270, 400, 350, 400)
    draw_lines(350, 400, 350, 600)


    # Drawing 1
    glColor3f(0.5, 1.0, 0.0)
    draw_lines(370, 400, 370, 600)


    # Drawing 0
    glColor3f(1.0, 0.5, 1.0)
    draw_lines(390, 600, 470, 600)
    draw_lines(390, 600, 390, 400)
    draw_lines(390, 400, 470, 400)
    draw_lines(470, 400, 470, 600)





glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)


glutMainLoop()


