from Camera import *

class FPSCam(Camera): 
    def __init__(self):
        
        self.pos = np.array([0.0, 2.0, 1.0])
        self.angle = 0   # 0 ~ 360 회전
        self.dir = self.get_direction()        

        super().__init__(eye=self.pos, at= self.pos + self.dir, up = np.array([0, 1, 0]) )
        self.update_camera()

    def get_direction(self):
        rad = np.deg2rad(self.angle)
        self.dir = np.array([np.cos(rad), 0, np.sin(rad)])
        return self.dir

    def update_camera(self):
        self.eye = self.pos
        self.at = self.pos + self.dir
        self.mark_dirty()


    def forward(self, step = 0.1):
        self.pos = self.pos + self.dir * step
        self.update_camera()

    def backward(self, step = 0.1):
        self.pos = self.pos - self.dir * step
        self.update_camera()

    def left(self, angle_step = 1.0):
        self.angle -= angle_step
        self.get_direction()
        self.update_camera()

    def right(self, angle_step = 1.0):
        self.angle += angle_step
        self.get_direction()
        self.update_camera()

