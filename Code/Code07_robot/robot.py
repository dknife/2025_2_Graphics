import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common

t = 0

main_camera = Camera.Camera()

def drawPart(width, height, depth):
    glPushMatrix()
    glScalef(width, height, depth)
    common.drawWireCube()
    glPopMatrix()

def initialize(window):
    glClearColor(0.6, 0.6, 0.6, 1.0)
    glLineWidth(2)
    glEnable(GL_DEPTH_TEST)

    main_camera.eye = np.array([-5,5,10])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

def display(window):
    global t

    t += 0.01
    angle = 45 * np.sin(t)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    common.drawPlane()
    common.drawAxes()

    glColor3f(1, 1, 1)    
    glTranslatef(0, 0.5, 0)
    drawPart(2, 1, 2) # 몸통

    # 부모 높이의 반만 올라온다.
    glTranslatef(0, 0.5, 0)
    glRotatef(angle, 0, 0, 1)
    # 내 길이의 반 올라간다.
    glTranslatef(0, 1.5, 0)
    drawPart(0.5, 3, 0.5) # 팔 1

    # 부모의 높이 반 올라가기
    glTranslatef(0, 1.5, 0)
    glRotatef(angle*0.5, 0, 0, 1)
    glTranslatef(0, 0.5, 0)
    drawPart(0.5, 1, 0.5) # 팔 2

    glPushMatrix()

    # 손1
    # 부모의 반
    glTranslatef(0, 0.5, 0)
    glRotatef(angle, 0, 0, 1)
    glTranslatef(0, 0.25, 0)
    drawPart(0.1, 0.5, 0.5)

    # 팔2의 변환 상태로 돌아간다...
    glPopMatrix()

    # 손2    
    # 부모의 반
    glTranslatef(0, 0.5, 0)
    glRotatef(-angle, 0, 0, 1)
    glTranslatef(0, 0.25, 0)
    drawPart(0.1, 0.5, 0.5)


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
