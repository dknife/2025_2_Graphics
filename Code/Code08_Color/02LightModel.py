import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common


main_camera = Camera.Camera()

# 전역 변수로 정점 좌표를 지정하자
p0 = [0., 5., 0.]
p1 = [-3., 1., 3.]
p2 = [3., 1., 3.]
p3 = [0., 1., -3.]
angle = 0

# 조명 계산에 필요한 데이터를 준비하자
# 재질: 물체의 특성
mat_ambient = [0.1, 0.1, 0.1, 1.0] # 주변광에 반응 (ambient material)
mat_diffuse = [1.0, 1.0, 0.0, 1.0] # 난반사광에 반응 (diffuse material)
mat_specular= [1.0, 1.0, 1.0, 1.0] # 정반사광에 반응 (specular material)
mat_shininess = [120] # 반질반질함 (shininess material)

# 광원 설정
lit_ambient = [0.0, 0.0, 0.0, 1.0] # 물체에 가해질 주변 광
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

def get_normal(p0, p1, p2):
    p0 = np.array(p0)
    p1 = np.array(p1)
    p2 = np.array(p2)
    u = p1 - p0
    v = p2 - p0
    N = np.cross(u, v)
    length = np.linalg.norm(N)
    N /= length
    return N


def initialize(window):
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glLineWidth(2)
    glEnable(GL_DEPTH_TEST)

    main_camera.eye = np.array([10, 10, 10])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

    LightSet()
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

def display(window):
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    main_camera.apply() 
    LightPositioning()

    common.drawAxes()
    common.drawPlane()
    angle += 1
    glRotatef(angle, 0, 1, 0)

    glBegin(GL_TRIANGLES)
    # face 1
    # Normal을 구하고 싶다!
    N = get_normal(p0, p1, p2)
    glNormal3fv(N)
    glColor3f(1, 0, 0)
    glVertex3fv(p0)
    glColor3f(0, 1, 0)
    glVertex3fv(p1)
    glColor3f(0, 0, 1)
    glVertex3fv(p2)

    # face 2
    N = get_normal(p0, p2, p3)
    glNormal3fv(N)
    glColor3f(1, 0, 0)
    glVertex3fv(p0)
    glColor3f(0, 1, 0)
    glVertex3fv(p2)
    glColor3f(0, 0, 1)
    glVertex3fv(p3)

    # face 3
    N = get_normal(p0, p3, p1)
    glNormal3fv(N)
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