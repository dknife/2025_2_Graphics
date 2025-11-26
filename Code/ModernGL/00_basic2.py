# xyz_triangle_rgb.py
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
import numpy as np
from myglfw import *

# 정점 데이터: 위치(x,y,z) + 색상(r,g,b)
vertices = np.array([
    # 위치          # 색상
     1.0,  0.0,  0.0,   1.0, 0.0, 0.0,   # X축 끝 → 빨강
     0.0,  1.0,  0.0,   0.0, 1.0, 0.0,   # Y축 끝 → 초록
     0.0,  0.0,  1.0,   0.0, 0.0, 1.0,   # Z축 끝 → 파랑
], dtype=np.float32)

# 쉐이더 (정적 카메라, 회전 없음)
vs = """
#version 460 core
layout(location=0) in vec3 aPos;
layout(location=1) in vec3 aColor;

out vec3 vColor;

uniform mat4 view;
uniform mat4 proj;

void main()
{
    gl_Position = proj * view * vec4(aPos, 1.0);
    vColor = aColor;
}
"""

fs = """
#version 460 core

float rand(float x) {
    return fract(sin(x) * 43758.5453123);
}

in vec3 vColor;
out vec4 fragColor;

void main()
{
    vec3 color = vColor;        // 읽기용 in 변수를 복사
    color.r = rand(color.r*color.g);    // 복사본 수정

    fragColor = vec4(color, 1.0);
}
"""

# 전역 변수
shader = None
vao = None
t = 0.0

def init_gl(window):
    global shader, vao

    # 쉐이더 컴파일
    shader = compileProgram(
        compileShader(vs, GL_VERTEX_SHADER),
        compileShader(fs, GL_FRAGMENT_SHADER)
    )

    # VAO/VBO 설정
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # 위치 속성
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(0))
    # 색상 속성
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(3*4))

    glBindVertexArray(0)
    glUseProgram(shader)

    # 고정된 뷰 & 투영 행렬 설정 (45도 시점에서 XYZ축 잘 보이게)
    view = np.array([
        [ 0.7071, -0.4082,  0.5774,  0.0],
        [ 0.0000,  0.8165,  0.5774,  0.0],
        [-0.7071, -0.4082,  0.5774,  0.0],
        [ 0.0000,  0.0000, -3.4641,  1.0]
    ], dtype=np.float32)

    proj = np.array([
        [ 1.7926,  0.0000,  0.0000,  0.0000],
        [ 0.0000,  2.4142,  0.0000,  0.0000],
        [ 0.0000,  0.0000, -1.0020, -1.0000],
        [ 0.0000,  0.0000, -0.2002,  0.0000]
    ], dtype=np.float32)

    glUniformMatrix4fv(glGetUniformLocation(shader, "view"), 1, GL_FALSE, view)
    glUniformMatrix4fv(glGetUniformLocation(shader, "proj"), 1, GL_FALSE, proj)

    glEnable(GL_DEPTH_TEST)

def display(window):
    global t
    t += 0.01

    glClearColor(0.1, 0.1, 0.12, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    view = np.array([
        [ np.sin(t), -0.4082,  0.5774,  0.0],
        [ 0.0000,  np.cos(t),  0.5774,  0.0],
        [-0.7071, -0.4082,  0.5774,  0.0],
        [ 0.0000,  0.0000, -3.4641,  1.0]
    ], dtype=np.float32)

    proj = np.array([
        [ 1.7926,  0.0000,  0.0000,  0.0000],
        [ 0.0000,  np.cos(t),  0.0000,  0.0000],
        [ 0.0000,  0.0000, -1.0020, -1.0000],
        [ 0.0000,  0.0000, -0.2002,  0.0000]
    ], dtype=np.float32)

    glUniformMatrix4fv(glGetUniformLocation(shader, "view"), 1, GL_FALSE, view)
    glUniformMatrix4fv(glGetUniformLocation(shader, "proj"), 1, GL_FALSE, proj)

    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)

def reshape(window, w, h):
    glViewport(0, 0, w, h)

def keyboard(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

# 메인
window = initialize_window(800, 600, "XYZ 삼각형 - R,G,B 꼭지점")
register_initGL(window, init_gl)
register_reshape(window, reshape)
register_keyboard(window, keyboard)
main_loop(window, display)