import glfw
from OpenGL.GL import *

import math

############################################################
# GLFW 윈도우 관리 코드
#
# 윈도우 생성함수
def initialize_window(w, h, window_title) :
    glfw.init() 
    win = glfw.create_window(w, h, window_title, None, None)
    glfw.make_context_current(win)
    return win

# 메인 루프 함수를 만들자
def main_loop(win_handle, gl_code):
    while not glfw.window_should_close(win_handle):
        gl_code()
        glfw.swap_buffers(win_handle)
        glfw.poll_events()

    glfw.destroy_window(win_handle)
    glfw.terminate()
############################################################

############################################################
## 3가지 핵심 그래픽 코드

# initialize: OpenGL 초기화
def initialize(window):
    glClearColor(0.0, 1.0, 1.0, 1.0) # 
    

# reshape: 창의 크기가 변경될 때 필요한 일
def reshape(window, w, h):
    glViewport(0, 0, w, h)

# display: 매 프레임마다 그릴 내용
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # 나무줄기
    glBegin(GL_QUADS)
    glColor3f(0.7, 0.4, 0.2)
    glVertex2f( 0.65, -0.2)
    glVertex2f( 0.65, -0.9)
    glVertex2f( 0.75, -0.9)
    glVertex2f( 0.75, -0.2)   
    glEnd()

    # 나뭇잎
    glBegin(GL_TRIANGLES)
    glColor3f(0.3, 0.9, 0.2)
    glVertex2f( 0.7, 1)
    glVertex2f( 0.5, -0.3)    
    glVertex2f( 0.9, -0.3)
    glEnd()

    
    glBegin(GL_QUADS)

    # 지붕
    glColor3f(0.0, 0.1, 0.2)
    glVertex2f(-1.0, -0.3)
    glVertex2f( 0.8, -0.3)
    glVertex2f( 0.5, 0.4)
    glVertex2f(-0.7, 0.4)
    
    # 벽    
    glColor3f(0.9, 0.9, 0.7)
    glVertex2f(-0.7, -0.3)
    glVertex2f(-0.7, -0.9)    
    glVertex2f( 0.5, -0.9)
    glVertex2f( 0.5, -0.3)    
    
    glEnd()

    #### 나는 간절히 원을 그리고 싶다
    center = [-0.5, 0.7]
    r = 0.2
    nPoints = 30
    
    angleStep = 2 * 3.14 / nPoints
    angle = 0
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    for i in range(nPoints):
        angle += angleStep 
        x = r*math.cos(angle) + center[0]
        y = r*math.sin(angle) + center[1]
        glVertex2f(x, y)    
    glEnd()

############################################################

def main() :
    ## 윈도우를 생성하자.
    window = initialize_window(500, 500, "my gl window")

    glfw.set_framebuffer_size_callback(window, reshape)

    # 초기화 코드
    initialize(window)

    ## 윈도가 사라지지 않게 메인 루프에 들어가자.
    #  메인 루프 내에서 처리될 display
    main_loop(window, display)

if __name__ == "__main__":
    main()