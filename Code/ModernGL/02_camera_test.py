# main.py
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
from Camera import Camera
from myglfw import *  

# 쉐이더 (이제 view × projection 제대로 곱함!)
vs = """
#version 460 core
layout(location=0) in vec3 aPos;
layout(location=1) in vec3 aColor;

uniform mat4 view;
uniform mat4 projection;

out vec3 vColor;

void main()
{
    gl_Position = projection * view * vec4(aPos, 1.0);
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
    color.r = rand(0.01*color.r*color.g);    // 복사본 수정

    fragColor = vec4(color, 1.0);
}
"""

# 정점 데이터: X축 빨강, Y축 초록, Z축 파랑
vertices = np.array([
     1.0, 0.0, 0.0,   1.0, 0.0, 0.0,   # X
     0.0, 1.0, 0.0,   0.0, 1.0, 0.0,   # Y
     0.0, 0.0, 1.0,   0.0, 0.0, 1.0    # Z
], dtype=np.float32)

# 전역 객체
shader = None
vao = None
camera = None

def init_gl(window):
    global shader, vao, camera

    # 쉐이더 컴파일
    shader = compileProgram(compileShader(vs, GL_VERTEX_SHADER),
                            compileShader(fs, GL_FRAGMENT_SHADER))
    glUseProgram(shader)

    # VAO / VBO
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # position
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(0))
    # color
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6*4, ctypes.c_void_p(3*4))

    glBindVertexArray(0)
    glEnable(GL_DEPTH_TEST)

    # 카메라 생성 (좋은 시점)
    camera = Camera()
    camera.look_at([0.0, 0.2, 1.5], [0, 0, 0], [0, 1, 0])

def reshape(window, w, h):
    glViewport(0, 0, w, h)
    camera.set_aspect(w, h)

def display(window):
    glClearColor(0.1, 0.1, 0.12, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    camera.apply(shader)          # 이 한 줄로 카메라 완전 적용!

    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)

def keyboard(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

# ─────────────────────────────────────
window = initialize_window(900, 700, "XYZ RGB Triangle – 완벽 현대식 PyOpenGL")
register_initGL(window, init_gl)
register_reshape(window, reshape)
register_keyboard(window, keyboard)
main_loop(window, display)