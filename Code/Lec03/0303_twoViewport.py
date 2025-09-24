import glfw
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트


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

def initialize(window):
    glClearColor(0.0, 0.0, 0.0, 1.0)

def myScene():
    glColor3f(0, 1, 1)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(0, 0.5, 0)
    glEnd()

    drawAxes()

def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 전체 창 크기 가져오기
    width, height = glfw.get_framebuffer_size(window)

    # 첫 번째 뷰포트: 왼쪽 절반, 기본 카메라 (앞에서 바라봄)
    glViewport(0, 0, width // 2, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    asp_ratio = (width // 2) / height
    range_val = 2.0
    glOrtho(-range_val * asp_ratio, range_val * asp_ratio, -range_val, range_val, -10, 10)  # z 범위 확장
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 3,  # eye position
              0, 0, 0,  # look at
              0, 1, 0)  # up vector

    myScene()

    # 두 번째 뷰포트: 오른쪽 절반, 다른 카메라 (측면에서 비스듬히 바라봄)
    glViewport(width // 2, 0, width // 2, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    asp_ratio = (width // 2) / height
    glOrtho(-range_val * asp_ratio, range_val * asp_ratio, -range_val, range_val, -10, 10)  # 동일한 프로젝션
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2, 2, 2,  # eye position (다른 위치)
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
    
    # Manually apply initial reshape (필요 없어짐, display에서 처리)
    # width, height = glfw.get_framebuffer_size(window)
    # reshape(window, width, height)
    
    # Call initialize
    initialize(window)
    
    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()