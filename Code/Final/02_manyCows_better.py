# main_cow_light.py
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
from Camera import Camera
from Mesh import Mesh
from Light import Light
from myglfw import *
import os

def load_shader_source(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# ────────── 전역 객체 ──────────
shader = None
camera = None
mesh = None
light = None

angle = 0.0

##########################################################################################
def shader_instancing():
    # init_gl() 안에 추가
    N = 100
    total_instances = N * N  # 10,000

    # 100x100 격자에 소 배치
    offsets = []
    interval = 2.0
    for i in range(N):
        for j in range(N):
            offsets.append([i * interval - N*interval/2, j * interval - N*interval/2])  # 예쁘게 중앙 정렬

    offsets = np.array(offsets, dtype=np.float32)

    # 인스턴스용 VBO 생성
    instance_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, instance_vbo)
    glBufferData(GL_ARRAY_BUFFER, offsets.nbytes, offsets, GL_STATIC_DRAW)

    # 기존 VAO에 인스턴스 속성 추가 (location = 2)
    glBindVertexArray(mesh.vao)

    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)
    ###############################################
    glVertexAttribDivisor(2, 1)   # 이게 핵심! 인스턴스별로 하나씩 끊어서 인스턴스에 전달
    ###############################################

    glBindVertexArray(0)
###################################################################################################

# ────────── OpenGL 초기화 ──────────
def init_gl(window):
    global shader, camera, mesh, light

    # 1. 먼저 셰이더 컴파일 (VAO 없이도 가능!)
    vert_path = os.path.join('./Final/manyCows_better/', 'vertex.vs')
    frag_path = os.path.join('./Final/manyCows_better/', 'frag.fs')

    vs_source = load_shader_source(vert_path)
    fs_source = load_shader_source(frag_path)

    vertex_shader = compileShader(vs_source, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fs_source, GL_FRAGMENT_SHADER)

    shader = compileProgram(vertex_shader, fragment_shader, validate = False)
    glUseProgram(shader)

    # 강제로 VAO 바인딩해서 validate 통과시키기
    dummy_vao = glGenVertexArrays(1)
    glBindVertexArray(dummy_vao)
    glValidateProgram(shader)  # 이제 통과됨!
    glBindVertexArray(0)

    # 이제 VAO 생성해도 됨 → 여기서부터 mesh 초기화!
    mesh = Mesh()
    mesh.loadMesh("./Final/cow.txt")
    mesh.setupGL()          # 이제 VAO 생성됨

    ####################################
    shader_instancing()
    ####################################

    # Light, Camera 등 나머지 초기화
    light = Light()
    light.add_light(0, position=[2.0, 13.0, 2.0, 0.0], ambient=[0.1,0.1,0.1],
                    diffuse=[1.0,1.0,0.0], specular=[1.0,1.0,1.0], shininess=120.0)
    light.add_light(1, position=[-2.0, 11.0, -2.0, 0.0], ambient=[0.1,0.1,0.1],
                    diffuse=[0.0,1.0,1.0], specular=[1.0,1.0,1.0], shininess=120.0)

    glEnable(GL_DEPTH_TEST)
    camera = Camera()

    

# ────────── 화면 크기 변화 ──────────
def reshape(window, w, h):
    glViewport(0,0,w,h)
    camera.set_aspect(w,h)

# ────────── 렌더링 ──────────
def display(window):
    global angle

    glClearColor(0.1,0.1,0.12,1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    angle += 0.3
    x = angle * np.pi / 180.0
    camera.eye = np.array([50.0 * np.sin(x), 5+1*np.sin(10.*x), 50.0 * np.cos(x)])
    camera.look_at(camera.eye, [0,0,0], [0,1,0])
    camera.apply(shader)

    # 카메라 위치 uniform 전달
    eyePosLoc = glGetUniformLocation(shader, "eyePos")
    glUniform3fv(eyePosLoc, 1, camera.eye)

    # Light uniform 전달
    data = light.get_active_light_data()
    for i in range(light.MAX_LIGHTS):
        prefix = f"lights[{i}]"
        glUniform4fv(glGetUniformLocation(shader, f"{prefix}.position"), 1, data['positions'][i])
        glUniform3fv(glGetUniformLocation(shader, f"{prefix}.ambient"), 1, data['ambient'][i])
        glUniform3fv(glGetUniformLocation(shader, f"{prefix}.diffuse"), 1, data['diffuse'][i])
        glUniform3fv(glGetUniformLocation(shader, f"{prefix}.specular"), 1, data['specular'][i])
        glUniform1f(glGetUniformLocation(shader, f"{prefix}.shininess"), data['shininess'][i])
        glUniform1i(glGetUniformLocation(shader, "lightActive["+str(i)+"]"), int(data['active'][i]))

    #한 번만 그리면 10,000마리 소가 동시에 나옴!!! ##########################################
    glBindVertexArray(mesh.vao)
    glDrawElementsInstanced(GL_TRIANGLES, mesh.nF * 3, GL_UNSIGNED_INT, None, 10000)
    glBindVertexArray(0)
    ######################################################################################

    #for i in range(100):
    #    for j in range(100):
    #        offsetLoc = glGetUniformLocation(shader, "offset")
    #        glUniform2fv(offsetLoc, 1, np.array([i*2, j*2], dtype=float))
    #
    #        mesh.draw()

# ────────── 키보드 이벤트 ──────────
def keyboard(window, key, scancode, action, mods):
    if key==glfw.KEY_ESCAPE and action==glfw.PRESS:
        glfw.set_window_should_close(window, True)

# ────────── 프로그램 실행 ──────────
window = initialize_window(900,700,"Cow Mesh with Phong Light")
register_initGL(window, init_gl)
register_reshape(window, reshape)
register_keyboard(window, keyboard)
main_loop(window, display)

