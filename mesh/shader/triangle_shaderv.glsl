layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;
layout(location = 2) in vec2 tCoord;

out vec3 fcolor;
out vec2 texCoord;
void main()
{
            gl_Position = vec4(position.xyz, 1.0);
            fcolor = color;
            texCoord = tCoord;

        
}


