layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;
layout(location = 2) in vec2 tCoord;

uniform mat4 transform;

out vec3 fcolor;
out vec2 texCoord;
void main()
{
            gl_Position = transform * vec4(position, 1.0) ;
            fcolor = color;
            texCoord = tCoord;

        
}


