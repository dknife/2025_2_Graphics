#version 330 core

struct Light {
    vec4 position;    // ← vec3 → vec4로 변경! (w 값 저장용)
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};

#define MAX_LIGHTS 8
uniform Light lights[MAX_LIGHTS];
uniform int lightActive[MAX_LIGHTS];

uniform vec3 eyePos;

in vec3 FragPos;
in vec3 Normal;
out vec4 fragColor;

void main()
{
    vec3 norm = normalize(Normal);
    vec3 viewDir = normalize(eyePos - FragPos);
    vec3 result = vec3(0.0);

    for(int i = 0; i < MAX_LIGHTS; i++) {
        if(lightActive[i] == 0) continue;

        vec3 lightDir;
        if (lights[i].position.w == 0.0) {
            // 방향광: position.xyz = 빛이 오는 방향 (w = 0)
            lightDir = normalize(lights[i].position.xyz);
        } else {
            // 점광원: position.xyz = 광원 위치 (w = 1)
            lightDir = normalize(lights[i].position.xyz - FragPos);
        }

        float diff = max(dot(norm, lightDir), 0.0);
        vec3 reflectDir = reflect(-lightDir, norm);
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), lights[i].shininess);

        vec3 ambient  = lights[i].ambient;
        vec3 diffuse  = lights[i].diffuse * diff;
        vec3 specular = lights[i].specular * spec;

        result += ambient + diffuse + specular;
    }

    fragColor = vec4(result, 1.0);
}