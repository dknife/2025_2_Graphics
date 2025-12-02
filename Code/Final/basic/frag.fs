#version 330 core
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

