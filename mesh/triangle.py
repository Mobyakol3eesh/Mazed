from OpenGL.GL import *
from core.opengl_buffers import openGLBuffer
from core.opengl_utilities import OpenGLUtilities
from mesh.mesh import Mesh

vertices = [
     0.5,  0.5, 0.0, #top right 
     0.5, -0.5, 0.0,  #bottom right
    
    -0.5, -0.5, 0.0,  #bottom left
    -0.5,  0.5, 0.0  #top left
        ]
indices = [
    0,1,3,
    1,2,3
]
vertexShaderSource = """
        layout(location = 0) in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """
fragmentShaderSource = """
        out vec4 color;
        void main()
        {
            color = vec4(0.2f, 0.4f, 0.3f, 1.0f);
        }
        """


class Triangle(Mesh):
    def __init__(self,vertices=vertices,indices=indices,vertexShaderSource=vertexShaderSource,fragmentShaderSource=fragmentShaderSource):
        super().__init__(vertices,indices, vertexShaderSource, fragmentShaderSource)
        
        

        
        




