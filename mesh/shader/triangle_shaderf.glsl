in vec3 ourcolor;
out vec4 fragColor;
in vec3 fragpos;
void main()
{
            fragColor = vec4(fragpos, 1.0f);
}