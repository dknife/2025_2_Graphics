from OpenGL.GL import *
from OpenGL.GLU import *


import numpy as np
           
class Mesh():
    def __init__(self):
        self.nV = 0
        self.nF = 0
        self.vBuffer = None
        self.iBuffer = None
        self.listNumber = 0
    
    ##  drawArrays, drawElements 사용하기
    def prepareForBufferRendering(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.vertexBuffer)

    def drawBuffer(self):
        glDrawElements(GL_TRIANGLES, self.nF * 3, GL_UNSIGNED_INT, self.idxBuffer)
        glColor3f(0, 0, 0)       

    def loadMesh(self, filename):
        with open(filename, 'rt') as inputFile:            
            # 정점의 개수를 읽는다.
            self.nV = int(next(inputFile))
            # 정점을 담을 버텍스 배열을 준비한다.
            self.vertexBuffer = np.zeros(shape = ( self.nV * 3, ), dtype = float)
            # self.nV 정점의 개수만큼 반복적으로 정점 정보를 읽는다.
            for i in range(self.nV):
                input_string = next(inputFile)
                start = i * 3
                end = start + 3
                self.vertexBuffer[start: end] = input_string.split()[0:3]

            # 정점의 좌표를 [-1, 1] 범위로 정규화한다.
            coordMin = self.vertexBuffer.min()
            coordMax = self.vertexBuffer.max()
            scale = max([coordMin, coordMax], key=abs)
            self.vertexBuffer /= scale

            # 면의 개수를 읽어 보자
            self.nF = int(next(inputFile))
            # 면을 구성하는 인덱스의 배열을 준비한다.
            self.idxBuffer = np.zeros( shape = ( self.nF * 3), dtype = int)
            # self.nF 면의 개수만큼 세 개의 색인(index)를 읽어들인다.
            for i in range(self.nF):
                input_string = next(inputFile)
                start = i * 3
                end = start + 3
                self.idxBuffer[start: end] = input_string.split()[1:4]
    
    def getVertex(self, idx):
        return self.vertexBuffer[ idx*3 : idx*3 + 3]  # idx*3 위치에서 3개의 점을 가져온다.
    