from myglfw import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self):
        #  카메라의 위치와 방향: gluLookAt의 인자
        self.eye = [0, 2, 3]
        self.at = [0, 0, 0] 
        self.up = [0, 1, 0]

        # 카메라 렌즈 설정: gluPerspective의 인자
        self.fovY = 60
        self.asp = 1  # width / height
        self.near = 0.1
        self.far = 100

    def applyCamera(self):
        # 렌즈 설정
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fovY, self.asp, self.near, self.far)

        # 카메라 위치와 방향 설정
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.eye[0], self.eye[1], self.eye[2],
                  self.at[0], self.at[1], self.at[2],
                  self.up[0], self.up[1], self.up[2])

### 카메라 인스턴스 만들기        
main_cam = Camera()
drawplane_list_number = None
vertexBuffer = None
colorBuffer = None
display_mode = 1

def drawPlane() :
    n = 300 # 그려지는 바둑판 모양의 땅을 몇 개의 점으로 나눌 것인가
    w = 300 # 그려지는 바둑판 모양의 땅이 너비
    d = w / (n-1) # 각 줄 사이의 간격
    
    startX = -w/2
    startZ = -w/2
    
    glBegin(GL_QUADS)
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0 :
                X = startX + i*d
                Z = startZ + j*d
                glVertex3f(X, 0, Z)
                glVertex3f(X+d, 0, Z)
                glVertex3f(X+d, 0, Z+d)
                glVertex3f(X, 0, Z+d)
    glEnd()

def drawPlane_buffers() :
    n = 300 # 그려지는 바둑판 모양의 땅을 몇 개의 점으로 나눌 것인가
    w = 300 # 그려지는 바둑판 모양의 땅이 너비
    d = w / (n-1) # 각 줄 사이의 간격
    
    startX = -w/2
    startZ = -w/2
    
    vBuffer = []
    cBuffer = []
    
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0 :
                X = startX + i*d
                Z = startZ + j*d
                vBuffer.append([X, 0, Z])
                cBuffer.append([1, 0, 0])
                vBuffer.append([X+d, 0, Z])
                cBuffer.append([0, 1, 0])
                vBuffer.append([X+d, 0, Z+d])
                cBuffer.append([0, 0, 1])
                vBuffer.append([X, 0, Z+d])
                cBuffer.append([1, 1, 1])

    return vBuffer, cBuffer



###################### GL Codes
def initialize(window):
    global vertexBuffer, colorBuffer, drawplane_list_number
    glClearColor(0, 0, 0.5, 1)

    # 디스플레이 리스트 준비
    drawplane_list_number = glGenLists(1)
    glNewList(drawplane_list_number, GL_COMPILE)
    drawPlane()
    glEndList()

    # 정점 버퍼를 준비
    vertexBuffer, colorBuffer = drawPlane_buffers()
    # 정점 버퍼를 GPU에 알려줌
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertexBuffer)
    # 색성 버퍼도 GPU에 알려줌
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colorBuffer)



def display(window):
    glClear(GL_COLOR_BUFFER_BIT)    

    main_cam.applyCamera()

    if display_mode == 1:
        glColor3f(1, 1, 0)
        drawPlane()
    elif display_mode == 2:
        glColor3f(0, 1, 1)
        glCallList(drawplane_list_number)    
    else:
        glDrawArrays(GL_QUADS, 0, len(vertexBuffer))

def reshape(window, w, h):
    glViewport(0, 0, w, h)

    global main_cam
    main_cam.asp = w / h
    main_cam.applyCamera()

def key_callback(window, key, scancode, action, modes):
    global main_cam, display_mode
    if action == glfw.PRESS or action == glfw.REPEAT:
        if glfw.KEY_W == key :
            main_cam.eye[2] -= 0.1
            main_cam.at[2] -= 0.1 
        elif glfw.KEY_S == key :
            main_cam.eye[2] += 0.1
            main_cam.at[2] += 0.1 
        elif glfw.KEY_A == key :
            main_cam.eye[0] -= 0.1
            main_cam.at[0] -= 0.1 
        elif glfw.KEY_D == key :
            main_cam.eye[0] += 0.1
            main_cam.at[0] += 0.1 
    if action == glfw.PRESS:
        if glfw.KEY_1 == key:
            print('immediate mode')
            display_mode = 1
        elif glfw.KEY_2 == key:
            print('display list mode')
            display_mode = 2
        elif glfw.KEY_3 == key:
            print('vertex buffer mode')
            display_mode = 3

    main_cam.applyCamera()

def main():
    window = initialize_window(500, 500, "my camera test")

    register_initGL(window, initialize)
    register_reshape(window, reshape)
    register_keyboard(window, key_callback)

    main_loop(window, display)

if __name__ == "__main__":
    main()

