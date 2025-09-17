import glfw
from OpenGL.GL import *

#########################################################

def initialize_window(w, h, window_title):
    if not glfw.init():
        return None
    window = glfw.create_window(w, h, window_title, None, None)
    if not window:
        glfw.terminate()
        print("window initialization failed")
        exit(0)

    glfw.make_context_current(window)
    return window

def main_loop(window, graphic_code):
    while not glfw.window_should_close(window):
        graphic_code()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()

#########################################################

def graphic_code():
    pass

def main():
    window = initialize_window(500, 500, "glfw window")    
    
    main_loop(window, graphic_code)


if __name__ == "__main__":
    main()

