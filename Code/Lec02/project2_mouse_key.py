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

points = []
current_primitive = GL_POINTS

def key_callback(window, key, scancode, action, mods):
    global current_primitive
    if action == glfw.PRESS:
        if glfw.KEY_0 <= key <= glfw.KEY_9:
            primitive_index = key - glfw.KEY_0
            print(f"number {primitive_index} key pressed")
            primitive = [
                GL_POINTS,
                GL_LINES, 
                GL_LINE_STRIP,
                GL_LINE_LOOP,
                GL_TRIANGLES,
                GL_TRIANGLE_STRIP,
                GL_TRIANGLE_FAN,
                GL_QUADS,
                GL_QUAD_STRIP,
                GL_POLYGON   
            ]
            current_primitive = primitive[primitive_index]            

def mouse_callback(window, button, action, mods):
    global points
    
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        mx, my = glfw.get_cursor_pos(window)
        ## OpenGL의 좌표로 변경해 보자
        w, h = glfw.get_framebuffer_size(window)
        nx = 2.0 * (mx/w) - 1.0
        ny = 1.0 - 2.0 * (my/h)

        print(mx, my)        
        points.append( [nx, ny, 0] )
        print("point added : ", nx, ny)

############################################################
## 3가지 핵심 그래픽 코드

# initialize: OpenGL 초기화
def initialize(window):
    glClearColor(0.0, 0.0, 0.0, 1.0) # 
    glPointSize(5)
    

# reshape: 창의 크기가 변경될 때 필요한 일
def reshape(window, w, h):
    glViewport(0, 0, w, h)

# display: 매 프레임마다 그릴 내용
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 0)
    glBegin(GL_POINTS)
    for point in points:
        glVertex3fv(point)
    glEnd()

    glColor3f(0, 1, 1)
    glBegin(current_primitive)
    for point in points:
        glVertex3fv(point)
    glEnd()
    
############################################################



def main() :
    ## 윈도우를 생성하자.
    window = initialize_window(500, 500, "my gl window")

    glfw.set_framebuffer_size_callback(window, reshape)
    glfw.set_mouse_button_callback(window, mouse_callback)
    glfw.set_key_callback(window, key_callback)

    # 초기화 코드
    initialize(window)

    ## 윈도가 사라지지 않게 메인 루프에 들어가자.
    #  메인 루프 내에서 처리될 display
    main_loop(window, display)

if __name__ == "__main__":
    main()