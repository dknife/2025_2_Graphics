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

points = []  # Global list to store points
current_primitive = GL_POINTS  # Default primitive

def initialize(window):
    glClearColor(0.0, 0.5, 0.5, 1.0)

def key_callback(window, key, scancode, action, mods):
    global current_primitive
    if action == glfw.PRESS:
        if glfw.KEY_0 <= key <= glfw.KEY_9:
            primitive_index = key - glfw.KEY_0
            primitives = [
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
            if primitive_index < len(primitives):
                current_primitive = primitives[primitive_index]
                print(f"Selected primitive {primitive_index}: {current_primitive}")

def mouse_callback(window, button, action, mods):
    global points
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        mx, my = glfw.get_cursor_pos(window)
        width, height = glfw.get_framebuffer_size(window)
        # Normalize to [-1, 1] range, accounting for y-inversion
        nx = 2.0 * (mx / width) - 1.0
        ny = 1.0 - 2.0 * (my / height)
        points.append([nx, ny, 0.0])
        print(f"mouse clicked at: ({mx}, {my})")
        print(f"Point added: ({nx:.2f}, {ny:.2f}, 0.0)")

def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(0, 1, 1)
    glBegin(current_primitive)
    for point in points:
        glVertex3fv(point)
    glEnd()

def reshape(window, width, height):
    glViewport(0, 0, width, height)


##########################################################

def main():
    window = initialize_window(500, 500, "glfw window")
    
    # Set up callbacks similar to GLUT
    glfw.set_framebuffer_size_callback(window, reshape)
    glfw.set_mouse_button_callback(window, mouse_callback)
    glfw.set_key_callback(window, key_callback)
    
    # Call initialize
    initialize(window)
    
    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()