from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

import numpy as np

TEXSIZE = 64
def createTexture():
    # 4 채널 UINT 이미지를 생성한다.
    # 각 픽셀의 값을 랜덤
    img = np.random.randint(0, 256, (TEXSIZE, TEXSIZE, 4), dtype = np.uint8)
    return img

def SetupTexture(img, w, h) :
    # GPU에 텍스처를 설정한다
    glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0,
                  GL_RGBA, GL_UNSIGNED_BYTE, img)

    # 텍스처 파라미터를 지정한다
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    
    # 텍스처를 사용할 수 있게 한다.
    glEnable( GL_TEXTURE_2D )

def loadTextureImage(filename) :

    img = Image.open(filename).convert("RGBA")
    w, h = img.size
    data = np.array(img, dtype = np.uint8)

    return data, w, h

def upload_texture(data, width, height, texture_unit = 0) :

    tex_id = glGenTextures(1)

    glActiveTexture(GL_TEXTURE0 + texture_unit)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                  GL_RGBA, GL_UNSIGNED_BYTE, data)
    
    # 텍스처 파라미터를 지정한다
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    print(f'texture uploaded to unit {texture_unit} (ID: {tex_id})')
    
    return tex_id

