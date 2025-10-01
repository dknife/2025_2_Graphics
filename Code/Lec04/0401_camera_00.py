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


def drawPlane():
    glBegin(GL_QUADS)
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0,  1)
    glVertex3f( 1, 0,  1)
    glVertex3f( 1, 0, -1)
    glEnd()

def display(window):
    
    main_cam.applyCamera()

    drawPlane()

def main():
    window = initialize_window(500, 500, "my camera test")

    main_loop(window, display)

if __name__ == "__main__":
    main()

