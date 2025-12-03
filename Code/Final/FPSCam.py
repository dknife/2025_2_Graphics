from Camera import *

class FPSCam(Camera): 
    def __init__(self):
        
        self.pos = np.array([0.0, 2.0, 1.0])
        self.dir = np.array([0.0, 0.0, -1.0])

        super().__init__(eye=self.pos, at= self.pos + self.dir, up = np.array([0, 1, 0]) )
