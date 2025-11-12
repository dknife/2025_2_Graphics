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