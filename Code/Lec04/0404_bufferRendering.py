import glfw
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트


class Camera :
    def __init__(self, eye=None, at=None, up=None) :
        # parameters for gluLookAt
        self.eye = eye if eye is not None else [0, 1, 3]
        self.at = at if at is not None else [0, 0, 0]
        self.up = up if up is not None else [0, 1, 0]

        # parameters for gluPerspective
        self.fovY = 60
        self.aspect = 1 # width/height
        self.near = 0.1
        self.far = 100

    def apply(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fovY, self.aspect, self.near, self.far)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.eye[0], self.eye[1], self.eye[2],
                  self.at[0], self.at[1], self.at[2],
                  self.up[0], self.up[1], self.up[2])

main_camera = Camera()


def drawPlane_buffers() :
    n = 500 # 그려지는 바둑판 모양의 땅을 몇 개의 점으로 나눌 것인가
    w = 50 # 그려지는 바둑판 모양의 땅이 너비
    d = w / (n-1) # 각 줄 사이의 간격
    
    v_buffer = []
    c_buffer = []

    startX = -w/2
    startZ = -w/2
    
    glColor3f(1, 1, 0)
    
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0 :
                X = startX + i*d
                Z = startZ + j*d
                v_buffer.append([X, 0, Z])
                c_buffer.append([1,1,0])
                v_buffer.append([X+d, 0, Z])
                c_buffer.append([0,1,1])
                v_buffer.append([X+d, 0, Z+d])
                c_buffer.append([1,0,1])
                v_buffer.append([X, 0, Z+d])
                c_buffer.append([1,1,1])

    return v_buffer, c_buffer

vertex_buffer = None
color_buffer = None

def initialize(window):
    global vertex_buffer, color_buffer
    glClearColor(0.0, 0.0, 0.0, 1.0)
    vertex_buffer, color_buffer = drawPlane_buffers()
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertex_buffer)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, color_buffer)


def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    main_camera.apply()
    glDrawArrays(GL_QUADS, 0,  len(vertex_buffer))


def reshape(window, width, height):
    glViewport(0, 0, width, height)
    main_camera.aspect = width / height
    main_camera.apply()

def key_callback(window, key, scancode, action, mods):
    global main_camera
    if action == glfw.PRESS  or action == glfw.REPEAT:
        if glfw.KEY_W == key :
            main_camera.eye[2] -= 0.05
            main_camera.at[2] -= 0.05            
        elif glfw.KEY_S == key :
            main_camera.eye[2] += 0.05
            main_camera.at[2] += 0.05
        elif glfw.KEY_D == key :
            main_camera.eye[0] += 0.05
            main_camera.at[0] += 0.05
        elif glfw.KEY_A == key :
            main_camera.eye[0] -= 0.05
            main_camera.at[0] -= 0.05

##########################################################

def main():
    window = initialize_window(500, 500, "camera test")

    register_initGL(window, initialize)
    register_reshape(window, reshape)    
    register_keyboard(window, key_callback)
    

    
    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()