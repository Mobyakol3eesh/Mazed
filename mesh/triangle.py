import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))


from OpenGL.GL import *
from core.opengl_buffers import openGLBuffer
from core.opengl_utilities import OpenGLUtilities

class Triangle():
    def __init__(self):
        self.vertices = [
            -0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0
        ]
        self.vertexShaderSource = """
        layout(location = 0) in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """
        self.fragmentShaderSource = """
        out vec4 color;
        void main()
        {
            color = vec4(1.0f, 1.0f, 1.0f, 1.0f);
        }
        """
        self.vertexShaderID = OpenGLUtilities.createShader(GL_VERTEX_SHADER, self.vertexShaderSource)
    
        self.fragmentShaderID = OpenGLUtilities.createShader(GL_FRAGMENT_SHADER, self.fragmentShaderSource)
   
        self.vertexBufferID, self.vertexArrayID = openGLBuffer(GL_ARRAY_BUFFER).createVertexBuffer(self.vertices, 0)

        
        




