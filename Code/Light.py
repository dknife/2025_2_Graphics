
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *

import common

#### 조명에 적용되는 기본적(default) 재질과 광원 색상
# 기본 재질
mat_ambient = [0, 0, 0, 1] 
mat_diffuse = [1, 1, 1, 1]
mat_specular = [1, 1, 1, 1]
mat_shininess = [120]

# 기본 광원 색상
lit_ambient = [0, 0, 0, 1]
lit_diffuse = [1, 1, 1, 1] 
lit_specular = [1, 1, 1, 1]

# 기본 광원 위치
lit_position = [1, 1, 1, 1]


class Light:

    MAX_LIGHTS = 8 # 조명의 최대 개수
    light_positions = np.ones ( (8,4), dtype=np.float32)


    def __init__(self) :
        self.lightOn = np.zeros(Light.MAX_LIGHTS, dtype=bool)


    def turnOn(self, lightID,
               mAmbient = mat_ambient, mDiffuse = mat_diffuse, mSpecular = mat_specular,
               lAmbient = lit_ambient, lDiffuse = lit_diffuse, lSpecular = lit_specular,
               Shininess = mat_shininess,
               lPosition = lit_position, spotDir = [0, -1, 0], spotCutoff = -1.0) :
        
        if lightID < Light.MAX_LIGHTS:
            glEnable(GL_LIGHT0 + lightID)
            self.lightOn[lightID] = True

            #### 재질과 광원 설정 ####
            glMaterialfv(GL_FRONT, GL_AMBIENT, mAmbient)
            glMaterialfv(GL_FRONT, GL_DIFFUSE, mDiffuse)
            glMaterialfv(GL_FRONT, GL_SPECULAR, mSpecular)
            glMaterialfv(GL_FRONT, GL_SHININESS, Shininess)

            glLightfv(GL_LIGHT0 + lightID, GL_AMBIENT, lAmbient)
            glLightfv(GL_LIGHT0 + lightID, GL_DIFFUSE, lDiffuse)
            glLightfv(GL_LIGHT0 + lightID, GL_SPECULAR, lSpecular)

            Light.light_positions[lightID] = lPosition

            ### spot light인 경우 이를 설정한다.
            if spotCutoff > 0.0: # spotlight로 설정
                spotDir = np.array( spotDir, dtype = np.float32)
                spotDir = spotDir / np.linalg.norm(spotDir)  # 정규화, 스포트 라이트가 쳐다보는 방향

                glLightfv(GL_LIGHT0 + lightID, GL_SPOT_DIRECTION, spotDir)
                glLightfv(GL_LIGHT0 + lightID, GL_SPOT_CUTOFF, spotCutoff)
        

    def turnOff(self, lightID) :
        if lightID < Light.MAX_LIGHTS:
            glDisable(GL_LIGHT0 + lightID)
            self.lightOn[lightID] = False

    def setLightPosition(self):
        for lightID in range(Light.MAX_LIGHTS):
            if self.lightOn[lightID]:
                glLightfv(GL_LIGHT0 + lightID, GL_POSITION, Light.light_positions[lightID])

        
