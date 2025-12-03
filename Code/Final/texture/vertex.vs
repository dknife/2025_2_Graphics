#version 330 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aNormal;
layout(location = 2) in vec2 aInstanceOffset;  // ← 인스턴스별 오프셋!

uniform mat4 view;
uniform mat4 projection;

out vec3 FragPos;
out vec3 Normal;

float rand(float x) {
    return fract(sin(x) * 43758.5453123);
}

void main()
{
    vec3 pos = aPos;
    pos.x += aInstanceOffset.x+0.01*rand(pos.x*aInstanceOffset.y);   // 각 소마다 다른 위치!
    pos.z += aInstanceOffset.y+0.01*rand(pos.y*aInstanceOffset.x);

    FragPos = pos;
    Normal = aNormal;
    gl_Position = projection * view * vec4(pos, 1.0);
}