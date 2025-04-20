layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;

uniform vec3 offset;
out vec3 ourcolor;
out vec3 fragpos;
void main()
{
            gl_Position = vec4(position.x + offset.x,-position.y + offset.y,position.z + offset.z, 1.0);
            ourcolor = color;
            fragpos = position;
}


