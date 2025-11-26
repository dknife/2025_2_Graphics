# main_mesh.py
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
from Camera import Camera
from myglfw import *
from Mesh import Mesh   # 방금 만든 Mesh 클래스

# 쉐이더: normal을 컬러로 사용
vs = """
#version 460 core
layout(location=0) in vec3 aPos;
layout(location=1) in vec3 aNormal;

uniform mat4 view;
uniform mat4 projection;
uniform float add_position;

out vec3 vColor;

float rand(float x) {
    return fract(sin(x) * 43758.5453123);
}

void main()
{
    float a = add_position;
    vec3 pos = aPos;
    pos.x = pos.x + a + 0.05*rand(pos.z + a);
    pos.z = pos.z + a + 0.05*rand(pos.x + a*a);
    gl_Position = projection * view * vec4(pos, 1.0);
    vColor = normalize(aNormal) * 0.5 + 0.5; // 법선을 [0,1] 범위 색상으로
}
"""

fs = """
#version 460 core
in vec3 vColor;
out vec4 fragColor;
void main() { fragColor = vec4(vColor, 1.0); }
"""

# 전역 객체
shader = None
camera = None
mesh = None
add_loc = 0

def init_gl(window):
    global shader, camera, mesh, add_loc

    # 쉐이더 컴파일
    shader = compileProgram(
        compileShader(vs, GL_VERTEX_SHADER),
        compileShader(fs, GL_FRAGMENT_SHADER)
    )
    glUseProgram(shader)
    add_loc = glGetUniformLocation(shader, "add_position")

    # Mesh 로딩
    mesh = Mesh()
    mesh.loadMesh("./cow.txt")   # cow.txt 파일
    mesh.setupGL()

    glEnable(GL_DEPTH_TEST)

    # 카메라 생성
    camera = Camera()
    camera.look_at([4.5, 2.5, 2.5], [0, 0, 0], [0, 1, 0])

def reshape(window, w, h):
    glViewport(0, 0, w, h)
    camera.set_aspect(w, h)

def display(window):
    global shader, add_loc

    glClearColor(0.1, 0.1, 0.12, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    camera.apply(shader)
    glUniform1f(add_loc, 0.0)
    mesh.draw()  # Mesh 렌더링    
    glUniform1f(add_loc, 1.0)
    mesh.draw()  # Mesh 렌더링
    glUniform1f(add_loc, 2.0)
    mesh.draw()  # Mesh 렌더링

def keyboard(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

# ─────────────────────────────────────
window = initialize_window(900, 700, "Cow Mesh – Modern OpenGL")
register_initGL(window, init_gl)
register_reshape(window, reshape)
register_keyboard(window, keyboard)
main_loop(window, display)
