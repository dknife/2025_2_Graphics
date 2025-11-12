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
    # img = createTexture()
    # SetupTexture(img, TEXSIZE, TEXSIZE)

    # img, w, h = loadTextureImage('photo2.png')
    # SetupTexture(img, w, h)

    ### multi texture
    data0, w0, h0 = loadTextureImage('photo.jpg')
    texture0 = upload_texture(data0, w0, h0, texture_unit = 0)
    
    data1, w1, h1 = loadTextureImage('photo2.png')
    texture1 = upload_texture(data1, w1, h1, texture_unit = 1)

    glMultiTexCoord2f(GL_TEXTURE0, 0, 0)

def display(window):
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    angle += 1
    glRotatef(angle, 0, 1, 0)
    step = angle*0.01

    how_many_stages = 2
    for i in range(how_many_stages) :
        glActiveTexture(GL_TEXTURE0 + i)
        glDisable(GL_TEXTURE_2D)

    glColor3f(1, 1, 1)
    common.drawAxes()
    common.drawPlane()

    for i in range(how_many_stages) :
        glActiveTexture(GL_TEXTURE0 + i)
        glEnable(GL_TEXTURE_2D)
        
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    
    glMultiTexCoord2f(GL_TEXTURE0, 0, 0+step)
    glMultiTexCoord2f(GL_TEXTURE1, 0+step, 0)
    glVertex3f(-2, 1, -2)
    
    glMultiTexCoord2f(GL_TEXTURE0, 1, 0+step)
    glMultiTexCoord2f(GL_TEXTURE1, 2+step, 0)
    glVertex3f( 2, 1, -2)
    
    glMultiTexCoord2f(GL_TEXTURE0, 1, 1+step)
    glMultiTexCoord2f(GL_TEXTURE1, 2+step, 2)
    glVertex3f( 2, 1,  2)
    
    glMultiTexCoord2f(GL_TEXTURE0, 0, 1+step)
    glMultiTexCoord2f(GL_TEXTURE1, 0+step, 2)
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