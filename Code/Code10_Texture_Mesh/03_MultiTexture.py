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

from Texture_Test import *


# 조명 계산에 필요한 데이터를 준비하자
# 재질: 물체의 특성
mat_ambient = [1.0, 1.0, 1.0, 1.0] # 주변광에 반응 (ambient material)
mat_diffuse = [1.0, 1.0, 1.0, 1.0] # 난반사광에 반응 (diffuse material)
mat_specular= [1.0, 1.0, 1.0, 1.0] # 정반사광에 반응 (specular material)
mat_shininess = [120] # 반질반질함 (shininess material)

# 광원 설정
lit_ambient = [0.1, 0.1, 0.1, 1.0] # 물체에 가해질 주변 광
lit_diffuse = [1.0, 1.0, 1.0, 1.0] # 난반사를 일으킬 빛의 색
lit_specular =[1.0, 1.0, 1.0, 1.0] # 정반사를 일으킬 빛의 색

lit_position = [1, 1, 1, 0] # 방향광 directional light

### 재질과 광원을 설정하는 작업을 수행하는 함수 구현
# 광원 설정: glLight
# 재질 설정: glMaterial
def LightSet():
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, lit_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lit_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lit_specular)

def LightPositioning():
    glLightfv(GL_LIGHT0, GL_POSITION, lit_position)

def initialize(window):
    glClearColor(0.6, 0.6, 0.6, 1.0)
    glEnable(GL_DEPTH_TEST)

    mymesh.loadMesh("./cow.txt")
    mymesh.prepareForBufferRendering()

    main_camera.eye = np.array([1,2,2])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

    LightSet()
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

   

    # pyOpenGL의 문제로 이렇게 한 번 부르고 사용하지 않고 디스플레이에서 이 함수를 사용하면  오류가 발생
    # meaningless call to avoid "invalid operation" error of glEnd()
    glMultiTexCoord2f(GL_TEXTURE1, 0, 0)




def display(window):
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    LightPositioning()

    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 0.0, 0.0, 1.0])
    common.drawPlane()

    glDisable(GL_LIGHTING)
    common.drawAxes()
    glEnable(GL_LIGHTING)

    angle += 1
    glRotatef(angle, 0, 1, 0)


    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 1.0, 0.0, 1.0])
    glColor3f(1, 1, 0)

    for i in range(3):
        glActiveTexture(GL_TEXTURE0 + i)
        glEnable(GL_TEXTURE_2D)

    mymesh.drawBuffer()

    for i in range(3):
        glActiveTexture(GL_TEXTURE0 + i)
        glDisable(GL_TEXTURE_2D)

    glColor3f(1,1,1)



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