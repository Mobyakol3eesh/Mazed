from OpenGL.GL import *
from mesh.triangle import Triangle 
from core.opengl_utilities import OpenGLUtilities
from core.opengl_buffers import openGLBuffer



class Mesh(Triangle):
    def __init__(self,vertices,indices,vertexShaderPath,fragmentShaderPath):
        super().__init__(vertices, indices, vertexShaderPath, fragmentShaderPath)
        