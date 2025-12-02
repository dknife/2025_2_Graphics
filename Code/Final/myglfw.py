import glfw

#########################################################

def initialize_window(w, h, window_title):
    if not glfw.init():
        return None
    
    # 이 4줄 순서와 내용 절대 건들지 마세요!!!
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)   # 이 줄이 생명줄!!!

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

def register_reshape(window, reshape_func):
    glfw.set_framebuffer_size_callback(window, reshape_func)
    
    # Manually apply initial reshape
    width, height = glfw.get_framebuffer_size(window)
    reshape_func(window, width, height)

def register_initGL(window, initialize_func):
    # Call initialize
    initialize_func(window)

def register_keyboard(window, key_callback):
    glfw.set_key_callback(window, key_callback)
#########################################################