# ModernLight.py
import numpy as np

class Light:
    MAX_LIGHTS = 8

    def __init__(self):
        self.active = [False] * self.MAX_LIGHTS
        # 기본 광원 속성
        self.positions = np.zeros((self.MAX_LIGHTS, 4), dtype=np.float32)
        self.ambient   = np.zeros((self.MAX_LIGHTS, 3), dtype=np.float32)
        self.diffuse   = np.zeros((self.MAX_LIGHTS, 3), dtype=np.float32)
        self.specular  = np.zeros((self.MAX_LIGHTS, 3), dtype=np.float32)
        self.spot_dir  = np.zeros((self.MAX_LIGHTS, 3), dtype=np.float32)
        self.spot_cutoff = np.full(self.MAX_LIGHTS, -1.0, dtype=np.float32)
        self.shininess = np.full(self.MAX_LIGHTS, 32.0, dtype=np.float32)

    def add_light(self, lightID, 
                  position=[1,1,1,0], 
                  ambient=[0,0,0], 
                  diffuse=[1,1,1], 
                  specular=[1,1,1], 
                  shininess=32.0,
                  spot_dir=[0,-1,0],
                  spot_cutoff=-1.0):
        """광원 등록"""
        if lightID >= self.MAX_LIGHTS:
            return

        self.active[lightID] = True
        self.positions[lightID] = np.array(position, dtype=np.float32)
        self.ambient[lightID]   = np.array(ambient, dtype=np.float32)
        self.diffuse[lightID]   = np.array(diffuse, dtype=np.float32)
        self.specular[lightID]  = np.array(specular, dtype=np.float32)
        self.shininess[lightID] = shininess
        self.spot_dir[lightID]  = np.array(spot_dir, dtype=np.float32)
        self.spot_cutoff[lightID] = spot_cutoff

    def remove_light(self, lightID):
        if lightID >= self.MAX_LIGHTS:
            return
        self.active[lightID] = False

    def get_active_light_data(self):
        """Shader에 전달할 데이터만 필터링"""
        return {
            'positions': self.positions,
            'ambient': self.ambient,
            'diffuse': self.diffuse,
            'specular': self.specular,
            'shininess': self.shininess,
            'spot_dir': self.spot_dir,
            'spot_cutoff': self.spot_cutoff,
            'active': np.array(self.active, dtype=np.int32)
        }


# 사용 예시
'''

light = Light()
light.add_light(0, position=[1,2,3,1], diffuse=[1,1,1])


data = light.get_active_light_data()
glUniform3fv(glGetUniformLocation(shader, "lightPositions"), light.MAX_LIGHTS, data['positions'][:, :3])
glUniform3fv(glGetUniformLocation(shader, "lightDiffuse"), light.MAX_LIGHTS, data['diffuse'])

'''