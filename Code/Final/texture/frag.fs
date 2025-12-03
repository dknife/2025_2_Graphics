#version 330 core

struct Light {
    vec4 position;    // w == 0.0 → 방향광, w == 1.0 → 점광원
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};

#define MAX_LIGHTS 8
uniform Light lights[MAX_LIGHTS];
uniform int lightActive[MAX_LIGHTS];
uniform vec3 eyePos;
uniform sampler2D sphereMap;

in vec3 FragPos;
in vec3 Normal;
out vec4 fragColor;

float rand(float x) {
    return fract(sin(x) * 43758.5453123);
}

void main()
{
    vec3 norm = normalize(Normal);
    norm.x += rand(norm.x)*0.2;
    norm.y += rand(norm.y)*0.2;

    vec3 viewDir = normalize(eyePos - FragPos);
    vec3 result = vec3(0.0);

    // 1. 조명 계산 (루프)
    for(int i = 0; i < MAX_LIGHTS; i++) {
        if(lightActive[i] == 0) continue;

        vec3 lightDir;
        if (lights[i].position.w == 0.0) {
            // 방향광: 빛이 오는 방향은 -position.xyz
            lightDir = normalize(lights[i].position.xyz);
        } else {
            // 점광원
            lightDir = normalize(lights[i].position.xyz - FragPos);
        }

        float diff = max(dot(norm, lightDir), 0.0);
        vec3 reflectDir = reflect(-lightDir, norm);
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), lights[i].shininess);

        result += lights[i].ambient +
                  lights[i].diffuse * diff +
                  lights[i].specular * spec;
    }

    // 2. 스피어맵 반사 
    float m = 2.0 * sqrt(norm.x*norm.x + norm.y*norm.y + (norm.z + 1.0)*(norm.z + 1.0));
    vec2 sphereUV = norm.xy / m + 0.5;
    vec3 envColor = texture(sphereMap, sphereUV).rgb;

    // 3. 조명 + 환경 반사 합성
    result = result * 0.1 + envColor * 0.9;  // 금속 느낌으로 조정
    // 또는 완전 금속: result = envColor;

    fragColor = vec4(result, 1.0);
}