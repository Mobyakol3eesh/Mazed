from OpenGL.GL import *
from core.opengl_utilities import OpenGLUtilities
import os 
class Shader:
    def __init__(self, vertexShaderPath, fragmentShaderPath):
        self.vertex_shader_source =  None
        self.fragment_shader_source = None
        self.__load(vertexShaderPath,fragmentShaderPath)
        self.vertexShaderID = OpenGLUtilities.createShader(GL_VERTEX_SHADER, self.vertex_shader_source)
        self.fragmentShaderID = OpenGLUtilities.createShader(GL_FRAGMENT_SHADER, self.fragment_shader_source)
        self.programID = OpenGLUtilities.create_program(self.vertexShaderID, self.fragmentShaderID)
        

    def __load(self, vertexShaderPath=None, fragmentShaderPath=None):
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        
        vertexShaderPath = base_path + vertexShaderPath
        fragmentShaderPath = base_path + fragmentShaderPath
        
        with open(vertexShaderPath, 'r') as file:
            self.vertex_shader_source = file.read() 

        with open(fragmentShaderPath, 'r') as file:
            self.fragment_shader_source = file.read()
    def use(self):
        glUseProgram(self.programID)