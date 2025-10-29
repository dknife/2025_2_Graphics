import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common
import Mesh
main_camera = Camera.Camera()
mymesh = Mesh.Mesh()
angle = 0

def initialize(window):
    glClearColor(0.6, 0.6, 0.6, 1.0)
    glEnable(GL_DEPTH_TEST)

    mymesh.loadMesh("./cow.txt")
    #mymesh.prepareDisplayList()
    mymesh.prepareForBufferRendering()

    main_camera.eye = np.array([3,4,5])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

def display(window):
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    common.drawAxes()

    # 이 지점에서 현재 모델뷰 행렬 모드이다.
    common.drawAxes()
    glColor3f(1, 1, 0)
    mymesh.drawBuffer()

    # 모델뷰 행렬을 변경하자
    glTranslatef(2, 0, 0)
    common.drawAxes()
    glColor3f(1, 0, 0)    
    mymesh.drawBuffer()

    # 모델뷰 행렬을 변경하자
    glTranslatef(0, 2, 0)
    glRotatef(180, 0, 0, 1)
    common.drawAxes()
    glColor3f(0, 1, 1)    
    mymesh.drawBuffer()

    # 모델뷰 행렬을 변경하자
    glTranslatef(2, 0, 0)
    glRotatef(-90, 0, 1, 0)
    glRotatef(180, 1, 0, 0)
    common.drawAxes()
    glColor3f(1, 1, 1)    
    mymesh.drawBuffer()






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