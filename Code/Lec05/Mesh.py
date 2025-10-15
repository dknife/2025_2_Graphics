from OpenGL.GL import *
from OpenGL.GLU import *


import numpy as np
           
class Mesh():
    def __init__(self):
        self.nV = 0
        self.nF = 0
        self.vBuffer = None
        self.iBuffer = None
    
    def loadMesh(self, filename):
        pass
    
    def getVertex(self, idx):
        pass
    
    def drawMesh(self):
        pass
