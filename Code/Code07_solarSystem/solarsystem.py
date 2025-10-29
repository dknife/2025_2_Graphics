import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common
import Sphere

main_camera = Camera.Camera()

t = 0
Sun = Sphere.Sphere(1)
Earth = Sphere.Sphere(0.2, 6, 6)
Moon = Sphere.Sphere(0.1, 5, 5)
Mars = Sphere.Sphere(0.2, 6, 6)

def drawPart(width, height, depth):
    glPushMatrix()
    glScalef(width, height, depth)
    common.drawWireCube()
    glPopMatrix()

def initialize(window):
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glLineWidth(2)
    glEnable(GL_DEPTH_TEST)

    main_camera.eye = np.array([-5,5,10])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

def display(window):
    global t
    t += 0.1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    common.drawAxes()

    glPushMatrix()
    glColor3f(1, 0, 0)
    glRotatef(t, 0, 1, 0)
    Sun.draw()
    glPopMatrix()

    glPushMatrix() # 지구계로 들어가기 전에 변환 기록
    
    ### 지구계
    glRotatef(t*2, 0, 1, 0) # 공전
    glTranslatef(5, 0, 0)  
    glPushMatrix()
    glRotatef(t*200, 0, 1, 0) # 자전
    glColor3f(0, 0.5, 1)
    Earth.draw()
    glPopMatrix()
    
    glRotatef(t*50, 0, 1, 0)   # 공전    
    glTranslatef(0.4, 0, 0)
    glColor3f(1, 1, 1)
    Moon.draw()

    glPopMatrix() # 지구계의 변환을 삭제

    glRotatef(t*5, 0, 1, 0) # 공전
    glTranslatef(7, 0, 0)  
    glRotatef(t*100, 0, 1, 0) # 자전
    glColor3f(1, 0.5, 0)
    Mars.draw()



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
