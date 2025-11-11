import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

from Texture_Test import *

import Camera
import common
main_camera = Camera.Camera()

def initialize(window):
    
    # Check texture unit support
    max_texture_units = glGetIntegerv(GL_MAX_TEXTURE_UNITS)
    print(f"Max texture units supported: {max_texture_units}")
    
    if max_texture_units < 2:
        print("ERROR: Your system doesn't support multi-texturing!")
        return
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    main_camera.eye = np.array([6,6,6])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

    ####### initialize texture #########
    # ex1
    # texImage = createTexture()
    # SetupTexture(texImage, TEXSIZE, TEXSIZE)
    # ex2
    # img, w, h = loadTextureImage('./Lec10_Texture/photo.jpg')
    # SetupTexture(img, w, h)

    data0, w0, h0 = loadTextureImage('./Lec10_Texture/photo.jpg')
    texture0 = upload_texture(data0, w0, h0, texture_unit=0)

    
    data1 = createTexture()
    texture1 = upload_texture(data1, TEXSIZE, TEXSIZE, texture_unit=1)   


    # pyOpenGL의 문제로 이렇게 한 번 부르고 사용하지 않고 디스플레이에서 이 함수를 사용하면  오류가 발생
    # meaningless call to avoid "invalid operation" error of glEnd()
    glMultiTexCoord2f(GL_TEXTURE1, 0, 0)



def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply()
    
    common.drawAxes()

    glEnable(GL_TEXTURE_2D)
    
    ##### draw a textured quad ######
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)

    # 첫 번째 꼭짓점
    glMultiTexCoord2f(GL_TEXTURE0, 0.0, 1.0)  # 텍스처 0 좌표
    glMultiTexCoord2f(GL_TEXTURE1, 0.0, 3.0)  # 텍스처 1 좌표
    glVertex3f(-2, 0,  2)

    # 두 번째 꼭짓점
    glMultiTexCoord2f(GL_TEXTURE0, 0.0, 0.0)  # 텍스처 0 좌표
    glMultiTexCoord2f(GL_TEXTURE1, 0.0, 0.0)  # 텍스처 1 좌표
    glVertex3f(-2, 0, -2)

    # 세 번째 꼭짓점
    glMultiTexCoord2f(GL_TEXTURE0, 1.0, 0.0)  # 텍스처 0 좌표
    glMultiTexCoord2f(GL_TEXTURE1, 3.0, 0.0)  # 텍스처 1 좌표
    glVertex3f(2, 0, -2)

    # 네 번째 꼭짓점
    glMultiTexCoord2f(GL_TEXTURE0, 1.0, 1.0)  # 텍스처 0 좌표
    glMultiTexCoord2f(GL_TEXTURE1, 3.0, 3.0)  # 텍스처 1 좌표
    glVertex3f(2, 0,  2)

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