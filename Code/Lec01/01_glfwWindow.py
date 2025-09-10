import glfw
from OpenGL.GL import *


def myGL():
    glClearColor(0.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # 삼각형 그리기
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, 0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, -0.5)
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glEnd()

def main():
    glfw.init()
    window = glfw.create_window(640, 480, "My First GLFW Window", None, None)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        ###################
        # OpenGL drawing code here
        myGL()
        ###################
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
    
