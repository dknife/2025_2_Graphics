
from OpenGL.GL import *
from PIL import Image
import numpy as np

class FixedFunctionTexture:

    def __init__(self, max_units = 8):
        self.max_units = max_units
        self.n_units = 0
        self.texture_ids = []
        self.gen_enabled = []
        self.gen_modes = []
    
    def add_unit(self, 
                 image_file = None, 
                 wrap_mode = GL_REPEAT, filter_mode = GL_LINEAR, 
                 auto_enable = False, auto_mode = GL_SPHERE_MAP):
        
        if self.n_units >= self.max_units:
            print("full") 
            return
        
        # 이미지 파일을 로드하는 일부터
        data, w, h = self._load_image(image_file)

        # 텍스처 생성
        tex_id = glGenTextures(1)
        unit = GL_TEXTURE0 + self.n_units

        glActiveTexture(unit)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, data)
        
        ### texture parameters
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, wrap_mode )
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, wrap_mode )
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, filter_mode )
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, filter_mode )

        # 텍스처 좌표 자동 설정 상태를 저장 
        self.gen_enabled.append(auto_enable)
        self.gen_modes.append(auto_mode if auto_enable else None)

        if auto_enable:
            glEnable(GL_TEXTURE_GEN_S)
            glEnable(GL_TEXTURE_GEN_T)
            glTexGenf(GL_S, GL_TEXTURE_GEN_MODE, auto_mode )
            glTexGenf(GL_T, GL_TEXTURE_GEN_MODE, auto_mode )

        self.texture_ids.append(tex_id)
        self.n_units += 1
        

    def enable_all(self):
        for i in range(self.n_units):
            glActiveTexture(GL_TEXTURE0 + i)
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_ids[i] )
            # TEX S,T Gen 복원
            if self.gen_enabled[i]:
                glEnable(GL_TEXTURE_GEN_S)
                glEnable(GL_TEXTURE_GEN_T)
                glTexGenf(GL_S, GL_TEXTURE_GEN_MODE, self.gen_modes[i] )
                glTexGenf(GL_T, GL_TEXTURE_GEN_MODE, self.gen_modes[i] )

    def disable_all(self):
        for i in range(self.n_units):
            glActiveTexture(GL_TEXTURE0 + i)
            glDisable(GL_TEXTURE_2D)
            if self.gen_enabled[i]:
                glDisable(GL_TEXTURE_GEN_S)
                glDisable(GL_TEXTURE_GEN_T)
                

    def _load_image(self, filename):
        if filename is None:
            return None, -1, -1
        
        img = Image.open(filename).convert("RGBA")
        w, h = img.size
        data = np.array(img, dtype=np.uint8).flatten()
        
        return data, w, h

        

        


        
