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

def main_loop(window, display_func):
    while not glfw.window_should_close(window):
        display_func(window)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.destroy_window(window)
    glfw.terminate()

#########################################################
# Three callback functions for OpenGL Graphics

def initialize(window):
    glClearColor(0.0, 0.5, 0.5, 1.0)

def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 0)
    glVertex3f(-1, 0, 0)
    glVertex3f( 1, 0, 0)
    glVertex3f( 0, 1, 0)
    glColor3f(0, 1, 1)
    glVertex3f(-1, 0.5, 0)
    glVertex3f( 1, 0.5, 0)
    glVertex3f( 0,-0.5, 0)
    glEnd()

def reshape(window, width, height):
    glViewport(0, 0, width, height)
    
##########################################################

def main():
    window = initialize_window(500, 500, "glfw window")
    
    # Set up callbacks similar to GLUT
    glfw.set_framebuffer_size_callback(window, reshape)
    
    # Call initialize
    initialize(window)
    
    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()