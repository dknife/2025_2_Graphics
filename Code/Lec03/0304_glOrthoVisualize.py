import glfw
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# 축 그리기
def drawAxes():
    glBegin(GL_LINES)
    # X
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    # Y
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)
    # Z
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)
    glEnd()

def drawTriangle():
    glColor3f(0, 1, 1)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5,-0.5, 0)
    glVertex3f( 0.5,-0.5, 0)
    glVertex3f( 0.0, 0.5, 0)
    glEnd()

def drawHelix():
    glColor3f(1, 1, 0)
    nPoints = 1000
    glBegin(GL_LINE_STRIP)
    for i in range(nPoints):
        angle = i / 10.0
        x, y = math.cos(angle), math.sin(angle)
        glVertex3f(x, y, angle / 10)
    glEnd()

def drawTriangles():
    glColor3f(1, 1, 0)
    nTriangles = 10
    step = 0.3 
    half = step * (nTriangles // 2)
    
    for i in range(nTriangles):
        glBegin(GL_LINE_LOOP)
        glVertex3f(-0.5, -0.5, -half + i*step)
        glVertex3f( 0.5, -0.5, -half + i*step)
        glVertex3f( 0.0,  0.5, -half + i*step)
        glEnd()

def drawBox(l, r, b, t, n, f):
    glColor3f(1, 1, 1)
    # 박스 전면
    glBegin(GL_LINE_LOOP)
    glVertex3f(l, t, n)
    glVertex3f(l, b, n)
    glVertex3f(r, b, n)
    glVertex3f(r, t, n)
    glEnd()
    # 박스 후면
    glBegin(GL_LINE_LOOP)
    glVertex3f(l, t, f)
    glVertex3f(l, b, f)
    glVertex3f(r, b, f)
    glVertex3f(r, t, f)
    glEnd()
    # 4개의 연결 선
    glBegin(GL_LINES)
    glVertex3f(l, t, n)
    glVertex3f(l, t, f)
    glVertex3f(l, b, n)
    glVertex3f(l, b, f)
    glVertex3f(r, b, n)
    glVertex3f(r, b, f)
    glVertex3f(r, t, n)   
    glVertex3f(r, t, f)
    glEnd()

l, r, b, t, n, f = -3, 3, -2, 2, -1, 1

def myScene():
    drawTriangles() #drawHelix()
    drawAxes()
    drawBox(l, r, b, t, n, f)


def initialize(window):
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display(window):
    glClear(GL_COLOR_BUFFER_BIT)
    w, h = glfw.get_framebuffer_size(window)

    aspect_ratio = (w // 2) / h
    

    # view 1
    glViewport(0, 0, w//2, h)    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(l*aspect_ratio, r*aspect_ratio, b, t, n, f)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()    
    
    myScene()

    # view 2
    glViewport(w//2, 0, w//2, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-4 * aspect_ratio, 4 * aspect_ratio, -4, 4, -10, 10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2, 2, 2,  # eye vector
              0, 0, 0,  # target vector
              0, 1, 0)  # up vector
    
    myScene()

def reshape(window, w, h) :
    pass
    

def key_callback(window, key, scancode, action, mods):
    global l, r, b, t, n, f
    if action == glfw.PRESS:
        if glfw.KEY_A == key:
            l -= 0.2
            r -= 0.2
        elif glfw.KEY_D == key:
            l += 0.2
            r += 0.2
        elif glfw.KEY_W == key:
            b += 0.2
            t += 0.2
        elif glfw.KEY_S == key:
            b -= 0.2
            t -= 0.2
        elif glfw.KEY_X == key:
            l += 0.2
            r -= 0.2
        elif glfw.KEY_Z == key:
            l -= 0.2
            r += 0.2
        elif glfw.KEY_Q == key:
            n += 0.2
            f += 0.2
        elif glfw.KEY_E == key:
            n -= 0.2
            f -= 0.2
            

def main():
    window = initialize_window(1000, 500, "my camera test")

    glfw.set_framebuffer_size_callback(window, reshape)
    glfw.set_key_callback(window, key_callback)

    w, h = glfw.get_framebuffer_size(window)
    reshape(window, w, h)

    initialize(window)
    main_loop(window, display)

if __name__ == "__main__":
    main()

