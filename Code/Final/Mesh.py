# ModernMesh.py
from OpenGL.GL import *
import numpy as np

class Mesh:
    def __init__(self):
        self.nV = 0
        self.nF = 0
        self.vertexBuffer = None
        self.normalBuffer = None
        self.idxBuffer = None

        self.vao = None
        self.vbo = None
        self.nbo = None
        self.ebo = None

    def loadMesh(self, filename):
        with open(filename, 'rt') as f:
            # 정점 읽기
            self.nV = int(next(f))
            self.vertexBuffer = np.zeros((self.nV, 3), dtype=np.float32)
            self.normalBuffer = np.zeros((self.nV, 3), dtype=np.float32)
            for i in range(self.nV):
                self.vertexBuffer[i] = np.array(next(f).split()[0:3], dtype=float)

            # 정규화
            coordMin = self.vertexBuffer.min()
            coordMax = self.vertexBuffer.max()
            scale = max(abs(coordMin), abs(coordMax))
            self.vertexBuffer /= scale

            # 면 읽기
            self.nF = int(next(f))
            self.idxBuffer = np.zeros((self.nF, 3), dtype=np.uint32)
            for i in range(self.nF):
                idx = np.array(next(f).split()[1:4], dtype=int)
                self.idxBuffer[i] = idx

                # 법선 계산 및 누적
                p0, p1, p2 = self.vertexBuffer[idx[0]], self.vertexBuffer[idx[1]], self.vertexBuffer[idx[2]]
                N = np.cross(p1 - p0, p2 - p0)
                self.normalBuffer[idx[0]] += N
                self.normalBuffer[idx[1]] += N
                self.normalBuffer[idx[2]] += N

            # 법선 정규화
            norms = np.linalg.norm(self.normalBuffer, axis=1)
            self.normalBuffer /= norms[:, np.newaxis]

    def setupGL(self):
        """VAO, VBO, EBO 생성 및 데이터 업로드"""
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.nbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)

        glBindVertexArray(self.vao)

        # Vertex
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertexBuffer.nbytes, self.vertexBuffer, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        # Normal
        glBindBuffer(GL_ARRAY_BUFFER, self.nbo)
        glBufferData(GL_ARRAY_BUFFER, self.normalBuffer.nbytes, self.normalBuffer, GL_STATIC_DRAW)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

        # Indices
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.idxBuffer.nbytes, self.idxBuffer, GL_STATIC_DRAW)

        glBindVertexArray(0)

    def draw(self):
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.nF * 3, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)
