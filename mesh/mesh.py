from OpenGL.GL import *
from core.opengl_utilities import OpenGLUtilities
from core.opengl_buffers import openGLBuffer

class Mesh():
    def __init__(self, vertices,indices, vertexShaderSource, fragmentShaderSource):
        self.vertices = vertices
        self.indices = indices
        self.vertexShaderID = OpenGLUtilities.createShader(GL_VERTEX_SHADER, vertexShaderSource)
        self.fragemtShaderID = OpenGLUtilities.createShader(GL_FRAGMENT_SHADER, fragmentShaderSource)
        self.program = OpenGLUtilities.create_program(self.vertexShaderID, self.fragemtShaderID)
        
    
        self.glBuffer = openGLBuffer()
        self.vertexBufferID = self.glBuffer.createVertexBuffer(self.vertices,0)
        self.indexBufferID = self.glBuffer.createIndexBuffer(self.indices,0)
        