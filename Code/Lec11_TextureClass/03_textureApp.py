import glfw
import numpy as np
from myglfw import *
from OpenGL.GL import *
from OpenGL.GLU import *  # 추가: gluLookAt을 사용하기 위해 GLU 임포트

import Camera
import common
import Mesh

folder_location = './'

main_camera = Camera.Camera()
mymesh = Mesh.Mesh()
angle = 0

from Light import Light
from Texture import FixedFunctionTexture

tex1 = None
tex2 = None


myLights = Light()

def initialize(window):
    global tex1, tex2

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    mymesh.loadMesh(folder_location + "cow.txt")
    mymesh.prepareForBufferRendering()

    main_camera.eye = np.array([3,3,3])
    main_camera.at = np.array([0,0,0])
    main_camera.up = np.array([0,1,0])

    
    glEnable(GL_LIGHTING)

    myLights.turnOn(0, lDiffuse=[0, 1, 1, 1], lPosition=[2, 2, 2, 1], spotDir=[0, -0.7, -1], spotCutoff=60)    
    myLights.turnOn(1, lDiffuse=[1, 1, 0, 1], lPosition=[2, 2, 0, 1], spotDir=[-1, -1, -2], spotCutoff=45.0)
    myLights.turnOn(2, lDiffuse=[1, 0, 0, 1],  lPosition=[0, 2, 1, 1], spotDir=[-0, -1, -1.5], spotCutoff=65.0)

    tex1 = FixedFunctionTexture(max_units= 8)
    tex2 = FixedFunctionTexture(max_units= 8)

    tex1.add_unit(folder_location+"spheremap.png", 
                  auto_enable=True, auto_mode=GL_SPHERE_MAP)
    
    tex2.add_unit(folder_location+'photo2.png',
                  auto_enable=True, auto_mode=GL_OBJECT_LINEAR)
    
    tex2.add_unit(folder_location+'spheremap.png',
                  auto_enable=True, auto_mode=GL_EYE_LINEAR)


def display(window):
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    
    main_camera.apply() 
    myLights.setLightPosition()
    
    common.drawPlane()

    glDisable(GL_LIGHTING)
    common.drawAxes()
    glEnable(GL_LIGHTING)

    angle += 1
    
    glPushMatrix()
    glRotatef(angle, 0, 1, 0)

    tex1.enable_all()
    mymesh.drawBuffer()
    tex1.disable_all()
    glPopMatrix()

        
    glPushMatrix()
    glTranslatef(1, 0, 0)
    glRotatef(angle, 0, 1, 0)

    tex2.enable_all()
    mymesh.drawBuffer()
    tex2.disable_all()
    glPopMatrix()
    


def reshape(window, width, height):
    glViewport(0, 0, width, height)
    main_camera.aspect = width / height
    main_camera.apply()

##########################################################

def main():
    window = initialize_window(500, 500, "camera test")

    register_initGL(window, initialize)
    register_reshape(window, reshape)    


    # Main loop calling display
    main_loop(window, display)


if __name__ == "__main__":
    main()