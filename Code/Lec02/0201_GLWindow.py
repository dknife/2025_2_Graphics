import glfw
from OpenGL.GL import *

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


## 그래픽 프로그램으로 개선하자
def graphic_code():
    print("graphics code here")

def main() :
    ## 윈도우를 생성하자.
    window = initialize_window(500, 500, "my gl window")

    ## 윈도가 사라지지 않게 메인 루프에 들어가자.
    main_loop(window, graphic_code)

if __name__ == "__main__":
    main()