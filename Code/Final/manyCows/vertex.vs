#version 330 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aNormal;

uniform mat4 view;
uniform mat4 projection;
uniform vec2 offset;   // ← offset은 uniform 으로 선언돼 있음 (OK)

out vec3 FragPos;
out vec3 Normal;

void main()
{
    vec3 pos = aPos;                    // ← 변수 선언 필수!
    pos.x = pos.x + offset.x;           // ← vec2는 .x, .y 로 접근 (또는 offset[0])
    pos.z = pos.z + offset.y;           // ← .y 또는 offset[1]

    FragPos = pos;
    Normal = aNormal;
    gl_Position = projection * view * vec4(pos, 1.0);
}