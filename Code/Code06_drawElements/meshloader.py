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
    glClearColor(0.0, 0.0, 0.2, 1.0)
    glEnable(GL_DEPTH_TEST)

    mymesh.loadMesh("./Code06/skull.txt")
    #mymesh.prepareDisplayList()
    mymesh.prepareForBufferRendering()

    main_camera.eye = np.array([1.2,1.2,1])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

def display(window):
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply()        
    common.drawPlane()
    common.drawAxes()

    glRotatef(angle, 0, 1, 0)
    angle += 1
    # mymesh.drawMesh()
    # mymesh.callDisplayList()
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