import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common

main_camera = Camera.Camera()

def initialize(window):
    glClearColor(0.6, 0.6, 0.6, 1.0)
    glLineWidth(2)
    glEnable(GL_DEPTH_TEST)

    main_camera.eye = np.array([2,2,6])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

def display(window):
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    common.drawPlane()
    common.drawAxes()

    glColor3f(1, 1, 1)
    common.drawWireCube()




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