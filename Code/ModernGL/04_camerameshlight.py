# main_cow_light.py
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
from Camera import Camera
from Mesh import Mesh
from Light import Light
from myglfw import *

# ────────── 쉐이더 ──────────
vs = """
#version 460 core
layout(location=0) in vec3 aPos;
layout(location=1) in vec3 aNormal;

uniform mat4 view;
uniform mat4 projection;

out vec3 FragPos;
out vec3 Normal;

void main()
{
    FragPos = aPos;
    Normal = aNormal;
    gl_Position = projection * view * vec4(aPos, 1.0);
}
"""

fs = """
#version 460 core
struct Light {
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};
#define MAX_LIGHTS 8
uniform Light lights[MAX_LIGHTS];
uniform int lightActive[MAX_LIGHTS];  // struct 밖으로 이동

uniform vec3 eyePos;  // ← 추가: 카메라 위치 전달

in vec3 FragPos;
in vec3 Normal;
out vec4 fragColor;

void main()
{
    vec3 norm = normalize(Normal);
    vec3 viewDir = normalize(eyePos - FragPos);
    vec3 result = vec3(0.0);

    for(int i=0; i<MAX_LIGHTS; i++){
        if(lightActive[i] == 0) continue;  // struct 대신 별도 uniform 사용

        vec3 lightDir = normalize(lights[i].position - FragPos);
        float diff = max(dot(norm, lightDir), 0.0);
        vec3 reflectDir = reflect(-lightDir, norm);
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), lights[i].shininess);

        vec3 ambient = lights[i].ambient;
        vec3 diffuse = lights[i].diffuse * diff;
        vec3 specular = lights[i].specular * spec;

        result += ambient + diffuse + specular;
    }

    fragColor = vec4(result, 1.0);
}
"""

# ────────── 전역 객체 ──────────
shader = None
camera = None
mesh = None
light = None

angle = 0.0

# ────────── OpenGL 초기화 ──────────
def init_gl(window):
    global shader, camera, mesh, light

    # 쉐이더 컴파일
    shader = compileProgram(
        compileShader(vs, GL_VERTEX_SHADER),
        compileShader(fs, GL_FRAGMENT_SHADER)
    )
    glUseProgram(shader)

    # Mesh 로딩
    mesh = Mesh()
    mesh.loadMesh("./ModernGL/cow.txt")
    mesh.setupGL()

    # Light 설정
    light = Light()
    light.add_light(0, position=[2.0, 3.0, 2.0, 1.0], ambient=[0.1,0.1,0.1],                    
                    diffuse=[1.0,1.0,0.0], specular=[1.0,1.0,1.0], shininess=120.0)
    
    light.add_light(1, position=[-2.0, 1.0, 2.0, 1.0], ambient=[0.1,0.1,0.1],                    
                    diffuse=[0.0,1.0,1.0], specular=[1.0,1.0,1.0], shininess=120.0)

    # Depth test
    glEnable(GL_DEPTH_TEST)

    # 카메라
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

    angle += 0.5
    x = angle * np.pi / 180.0
    camera.eye = np.array([3.0 * np.sin(x), 1.5, 3.0 * np.cos(x)])
    camera.look_at(camera.eye, [0,0,0], [0,1,0])
    camera.apply(shader)

    # 카메라 위치 uniform 전달
    eyePosLoc = glGetUniformLocation(shader, "eyePos")
    glUniform3fv(eyePosLoc, 1, camera.eye)

    # Light uniform 전달
    data = light.get_active_light_data()
    for i in range(light.MAX_LIGHTS):
        prefix = f"lights[{i}]"
        glUniform3fv(glGetUniformLocation(shader, f"{prefix}.position"), 1, data['positions'][i][:3])
        glUniform3fv(glGetUniformLocation(shader, f"{prefix}.ambient"), 1, data['ambient'][i])
        glUniform3fv(glGetUniformLocation(shader, f"{prefix}.diffuse"), 1, data['diffuse'][i])
        glUniform3fv(glGetUniformLocation(shader, f"{prefix}.specular"), 1, data['specular'][i])
        glUniform1f(glGetUniformLocation(shader, f"{prefix}.shininess"), data['shininess'][i])
        glUniform1i(glGetUniformLocation(shader, "lightActive["+str(i)+"]"), int(data['active'][i]))


    mesh.draw()

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
