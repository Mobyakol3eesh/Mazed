in vec3 fcolor;
in vec2 texCoord;
out vec4 fragColor;



uniform sampler2D texture0;
uniform sampler2D texture1;

void main()
{
    fragColor = mix(texture(texture0, texCoord), texture(texture1, texCoord), 0.2);
}