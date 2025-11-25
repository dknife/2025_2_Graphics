# Camera.py (OpenGL 표준 lookAt 적용 버전)
import numpy as np
from OpenGL.GL import *
import math

def perspective(fov_y: float, aspect: float, near: float, far: float) -> np.ndarray:
    """OpenGL 표준 perspective projection"""
    f = 1.0 / math.tan(math.radians(fov_y) / 2.0)
    nf = 1.0 / (near - far)
    proj = np.array([
        [f / aspect, 0.0, 0.0,               0.0],
        [0.0,        f,   0.0,               0.0],
        [0.0,        0.0, (far + near) * nf, 2 * far * near * nf],
        [0.0,        0.0, -1.0,              0.0]
    ], dtype=np.float32)
    return proj.T  # GLSL column-major 맞춤

def look_at(eye, at, up) -> np.ndarray:
    """OpenGL 표준 lookAt view matrix"""
    eye = np.array(eye, dtype=np.float32)
    at  = np.array(at , dtype=np.float32)
    up  = np.array(up , dtype=np.float32)

    f = at - eye
    f /= np.linalg.norm(f) + 1e-8

    r = np.cross(f, up)
    r /= np.linalg.norm(r) + 1e-8

    u = np.cross(r, f)

    view = np.identity(4, dtype=np.float32)
    view[0, :3] = r
    view[1, :3] = u
    view[2, :3] = -f
    # translation 부분: -eye를 rotation으로 변환
    view[:3, 3] = -np.dot(view[:3, :3], eye)

    return view.T  # GLSL column-major 맞춤

class Camera:
    def __init__(self, eye=None, at=None, up=None):
        self.eye = np.array(eye or [0, 1, 3], dtype=np.float32)
        self.at  = np.array(at  or [0, 0, 0], dtype=np.float32)
        self.up  = np.array(up  or [0, 1, 0], dtype=np.float32)

        self.fovY   = 60.0
        self.aspect = 1.0
        self.near   = 0.1
        self.far    = 100.0

        self._view = None
        self._proj = None
        self._dirty = True

    def mark_dirty(self):
        self._dirty = True

    def look_at(self, eye, at, up=None):
        self.eye = np.array(eye, dtype=np.float32)
        self.at  = np.array(at , dtype=np.float32)
        if up is not None:
            self.up = np.array(up, dtype=np.float32)
        self.mark_dirty()

    def set_aspect(self, w, h):
        self.aspect = w / max(h, 1)
        self.mark_dirty()

    def _update(self):
        if not self._dirty: return
        self._proj = perspective(self.fovY, self.aspect, self.near, self.far)
        self._view = look_at(self.eye, self.at, self.up)
        self._dirty = False

    def apply(self, program):
        self._update()
        v = glGetUniformLocation(program, "view")
        p = glGetUniformLocation(program, "projection")
        if v != -1:
            glUniformMatrix4fv(v, 1, GL_FALSE, self._view)
        if p != -1:
            glUniformMatrix4fv(p, 1, GL_FALSE, self._proj)
