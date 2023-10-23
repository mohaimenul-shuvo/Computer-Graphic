import random
gl.glClear(gl.GL_COLOR_BUFFER_BIT)
gl.glPointSize(5)
gl.glBegin(gl.GL_POINTS)
x=1
y=-1
for i in range(50):
  gl.glVertex2f(x*(random.random()),y*(random.random()))
  x=x*(-1)
  y=y*(-1)


gl.glEnd()


#
img_buf = gl.glReadPixelsub(0, 0, WIDTH, HEIGHT, gl.GL_RGB, gl.GL_UNSIGNED_BYTE)
img = np.frombuffer(img_buf, np.uint8).reshape(HEIGHT, WIDTH, 3)[::-1]
show.image(img/255.0)
#