import glfw
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트
import math

# Three callback functions for OpenGL Graphics

def drawAxes():
    glBegin(GL_LINES)
    # x축 (0,0,0) - (1,0,0)
    glColor3f(1, 0, 0) # 빨간색
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    # y축
    glColor3f(0, 1, 0) # 녹색
    glVertex3f(0,0,0)
    glVertex3f(0,1,0)
    # z축
    glColor3f(0, 0, 1) # 파란색
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)
    glEnd()
    glColor3f(1,1,1) # 흰색으로 복원

def drawHelix():
    glColor3f(1,1,1)
    glBegin(GL_LINE_STRIP)
    for i in range(1000):
        angle = i/10
        x, y = math.cos(angle), math.sin(angle)
        glVertex3f(x, y, -angle/10)
    glEnd()

def drawFrustum(l, r, b, t, n, f): 
    L = l * (f/n)
    R = r * (f/n)
    B = b * (f/n)
    T = t * (f/n)
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    # 앞면
    glVertex3f(l,t,-n)
    glVertex3f(l,b,-n)
    glVertex3f(r,b,-n)
    glVertex3f(r,t,-n)
    glEnd()
    glBegin(GL_LINE_LOOP)
    # 뒷면
    glVertex3f(L,T,-f)
    glVertex3f(L,B,-f)
    glVertex3f(R,B,-f)
    glVertex3f(R,T,-f)
    glEnd()

    # 모서리 연결선 4개
    glBegin(GL_LINES)       
    glVertex3f(l,t,-n)
    glVertex3f(L,T,-f) 
    glVertex3f(l,b,-n)
    glVertex3f(L,B,-f)   
    glVertex3f(r,b,-n)
    glVertex3f(R,B,-f)   
    glVertex3f(r,t,-n)
    glVertex3f(R,T,-f)
    glEnd()


def initialize(window):
    glClearColor(0.0, 0.0, 0.0, 1.0)

def myScene():
    drawAxes()
    drawHelix()
    drawFrustum(l, r, b, t, n, f)

l, r, b, t, n, f = -1, 1, -1, 1, 1.5, 5.5

def key_callback(window, key, scancode, action, mods):
    global l, r, b, t, n, f
    if action == glfw.PRESS:
        if glfw.KEY_A == key :
            l -= 0.1
            r -= 0.1
        elif glfw.KEY_D == key :
            l += 0.1
            r += 0.1

def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 전체 창 크기 가져오기
    width, height = glfw.get_framebuffer_size(window)

    # 첫 번째 뷰포트: 왼쪽 절반, 기본 카메라 (앞에서 바라봄)
    glViewport(0, 0, width // 2, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(l, r, b, t, n, f)  # z 범위 확장
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    

    myScene()

    # 두 번째 뷰포트: 오른쪽 절반, 다른 카메라 (측면에서 비스듬히 바라봄)
    glViewport(width // 2, 0, width // 2, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -100, 100)  # z 범위 확장
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(50, 10, 15,  # eye position (다른 위치)
              0, 0, 0,  # look at
              0, 1, 0)  # up vector

    myScene()


def reshape(window, width, height):
    # reshape는 더 이상 전체 프로젝션을 설정하지 않음; display에서 처리
    pass  # 필요 시 다른 로직 추가 가능
    
##########################################################

def main():
    window = initialize_window(1000, 500, "glfw window")
    
    # Set up callbacks similar to GLUT
    glfw.set_framebuffer_size_callback(window, reshape)
    glfw.set_key_callback(window, key_callback)
    
    # Manually apply initial reshape (필요 없어짐, display에서 처리)
    # width, height = glfw.get_framebuffer_size(window)
    # reshape(window, width, height)
    
    # Call initialize
    initialize(window)
    
    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()