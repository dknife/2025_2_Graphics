import glfw
from myglfw import *
from OpenGL.GL import *


# Three callback functions for OpenGL Graphics

def drawAxes():
    glBegin(GL_LINES)
    # x축 (0,0,0) - (1,0,0)
    glColor3f(1, 0, 0) # 빨간색
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    # y축
    glColor(0, 1, 0) # 녹색
    glVertex3f(0,0,0)
    glVertex3f(0,1,0)
    # z축
    glColor(0, 0, 1) # 파란색
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)
    glEnd()
    glColor3f(1,1,1) # 흰색으로 복원

def initialize(window):
    glClearColor(0.0, 0.0, 0.0, 1.0)

def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(0, 1, 1)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(0, 0.5, 0)
    glEnd()

    drawAxes()


def reshape(window, width, height):
    glViewport(0, 0, width, height)
    aspRatio = width / height # 종횡비를 계산한다.
    range = 2.0
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-range*aspRatio, range*aspRatio, -range, range, -1, 1)
    
##########################################################

def main():
    window = initialize_window(500, 500, "glfw window")
    
    # Set up callbacks similar to GLUT
    glfw.set_framebuffer_size_callback(window, reshape)
    
    # Manually apply initial reshape
    width, height = glfw.get_framebuffer_size(window)
    reshape(window, width, height)
    
    # Call initialize
    initialize(window)
    
    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()