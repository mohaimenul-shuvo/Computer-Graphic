gl.glClear(gl.GL_COLOR_BUFFER_BIT)
gl.glPointSize(5)
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(0, 1)
gl.glVertex2f(-.7, .7)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(0, 1)
gl.glVertex2f(.7, .7)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.7, .7)
gl.glVertex2f(.7, .7)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.7, .7)
gl.glVertex2f(-.7, -.7)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(.7, .7)
gl.glVertex2f(.7, -.7)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.7, -.7)
gl.glVertex2f(.7, -.7)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.5, .5)
gl.glVertex2f(-.2, .5)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.5, .5)
gl.glVertex2f(-.5, .2)
gl.glEnd()

gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.2, .5)
gl.glVertex2f(-.2, .2)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.2, .2)
gl.glVertex2f(-.5, .2)
gl.glEnd()

gl.glBegin(gl.GL_LINES)
gl.glVertex2f(.5, .5)
gl.glVertex2f(.2, .5)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(.5, .5)
gl.glVertex2f(.5, .2)
gl.glEnd()

gl.glBegin(gl.GL_LINES)
gl.glVertex2f(.2, .5)
gl.glVertex2f(.2, .2)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(.2, .2)
gl.glVertex2f(.5, .2)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.2, .1)
gl.glVertex2f(.2, .1)
gl.glEnd()

gl.glBegin(gl.GL_LINES)
gl.glVertex2f(.2, .1)
gl.glVertex2f(.2, -.6)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(-.2, .1)
gl.glVertex2f(-.2, -.6)
gl.glEnd()
gl.glBegin(gl.GL_LINES)
gl.glVertex2f(.2, -.6)
gl.glVertex2f(-.2, -.6)
gl.glEnd()
gl.glBegin(gl.GL_POINTS)
gl.glVertex2f(.1, -.4)

gl.glEnd()
#
img_buf = gl.glReadPixelsub(0, 0, WIDTH, HEIGHT, gl.GL_RGB, gl.GL_UNSIGNED_BYTE)
img = np.frombuffer(img_buf, np.uint8).reshape(HEIGHT, WIDTH, 3)[::-1]
show.image(img / 255.0)
#


