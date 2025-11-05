import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common


main_camera = Camera.Camera()

# 전역 변수로 정점 좌표를 지정하자
p0 = [0, 5, 0]
p1 = [-3, 1, 3]
p2 = [3, 1, 3]
p3 = [0, 1, -3]

angle = 0

def initialize(window):
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glLineWidth(2)
    glEnable(GL_DEPTH_TEST)

    main_camera.eye = np.array([10, 10, 10])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

def display(window):
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    common.drawAxes()
    angle += 1
    glRotatef(angle, 0, 1, 0)

    glBegin(GL_TRIANGLES)
    # face 1
    glColor3f(1, 0, 0)
    glVertex3fv(p0)
    glColor3f(0, 1, 0)
    glVertex3fv(p1)
    glColor3f(0, 0, 1)
    glVertex3fv(p2)

    # face 2
    glColor3f(1, 0, 0)
    glVertex3fv(p0)
    glColor3f(0, 1, 0)
    glVertex3fv(p2)
    glColor3f(0, 0, 1)
    glVertex3fv(p3)

    # face 3
    glColor3f(1, 0, 0)
    glVertex3fv(p0)
    glColor3f(0, 1, 0)
    glVertex3fv(p3)
    glColor3f(0, 0, 1)
    glVertex3fv(p1)

    glEnd()

    

def reshape(window, width, height):
    glViewport(0, 0, width, height)
    main_camera.aspect = width / height
    main_camera.apply()

##########################################################

def main():
    window = initialize_window(500, 500, "camera test")

    register_initGL(window, initialize)
    register_reshape(window, reshape)    


    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()