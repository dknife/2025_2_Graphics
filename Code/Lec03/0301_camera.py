import glfw
from myglfw import *
from OpenGL.GL import *

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

def initialize(window):
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display(window):
    glClear(GL_COLOR_BUFFER_BIT)

    drawAxes()
    drawTriangle()

def reshape(window, w, h) :
    glViewport(0, 0, w, h)


def main():
    window = initialize_window(500, 500, "my camera test")

    glfw.set_framebuffer_size_callback(window, reshape)

    initialize(window)
    main_loop(window, display)

if __name__ == "__main__":
    main()

