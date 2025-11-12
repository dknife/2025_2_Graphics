import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common

from Texture_Test import *


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

    main_camera.eye = np.array([3, 3, 3])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

    ### 텍스처를 설정하자 
    img = createTexture()
    SetupTexture(img, TEXSIZE, TEXSIZE)

def display(window):
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    angle += 1
    glRotatef(angle, 0, 1, 0)

    glDisable(GL_TEXTURE_2D)
    common.drawAxes()
    common.drawPlane()

    glEnable(GL_TEXTURE_2D)
    
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    
    glTexCoord2f(0, 0)
    glVertex3f(-2, 1, -2)
    
    glTexCoord2f(3, 0)
    glVertex3f( 2, 1, -2)
    
    glTexCoord2f(3, 3)
    glVertex3f( 2, 1,  2)
    
    glTexCoord2f(0, 3)
    glVertex3f(-2, 1,  2)
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