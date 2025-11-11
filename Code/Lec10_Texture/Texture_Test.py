from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트
from PIL import Image
    
import numpy as np

TEXSIZE = 64
def createTexture():
    return np.random.randint(0, 256, (TEXSIZE, TEXSIZE, 4), dtype=np.uint8)

def SetupTexture(img_data, width, height):
    glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                  GL_RGBA, GL_UNSIGNED_BYTE, img_data )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST )

    glEnable( GL_TEXTURE_2D )
    
def loadTextureImage(filename):
    print(f"Loading texture: {filename}")
    
    # 1. Open + force RGBA (adds alpha if missing)
    img = Image.open(filename).convert("RGBA")
    width, height = img.size
    # 2. Convert to NumPy array (H×W×4, uint8)
    data = np.array(img, dtype=np.uint8)

    width, height = img.size
    return data, width, height

################## multi texture를 사용할 수 있도록 업로드
def upload_texture(data, width, height, texture_unit):
        
    tex_id = glGenTextures(1)

    glActiveTexture(GL_TEXTURE0 + texture_unit)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    print(f"Texture uploaded to unit {texture_unit} (ID: {tex_id})")
    return tex_id
    