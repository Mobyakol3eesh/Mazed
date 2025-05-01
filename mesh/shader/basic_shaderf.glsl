
in vec2 texCoord;


out vec4 fragColor;


uniform bool isTextured;
uniform vec3 glColor;
uniform sampler2D texture0;
uniform sampler2D texture1;

void main()
{
    
    fragColor = isTextured ? 
        mix(texture(texture0, texCoord), texture(texture1, texCoord), 0.2) : 
        vec4(glColor, 1.0);
}