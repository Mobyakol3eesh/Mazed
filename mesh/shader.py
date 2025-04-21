from OpenGL.GL import *
from core.opengl_utilities import OpenGLUtilities
import os 
from glm import *
class Shader:
    def __init__(self, ShaderName=None):
        self.vertex_shader_source =  None
        self.fragment_shader_source = None
        self.__load(ShaderName)
        self.vertexShaderID = OpenGLUtilities.createShader(GL_VERTEX_SHADER, self.vertex_shader_source)
        self.fragmentShaderID = OpenGLUtilities.createShader(GL_FRAGMENT_SHADER, self.fragment_shader_source)
        self.programID = OpenGLUtilities.create_program(self.vertexShaderID, self.fragmentShaderID)
        self.use()
        

    def __load(self, ShaderName=None):
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        
        vertexShaderPath = os.path.join(base_path, "shader", f"{ShaderName}v.glsl")
        fragmentShaderPath = os.path.join(base_path, "shader", f"{ShaderName}f.glsl")
        
        with open(vertexShaderPath, 'r') as file:
            self.vertex_shader_source = file.read() 

        with open(fragmentShaderPath, 'r') as file:
            self.fragment_shader_source = file.read()
            
    def use_uniform(self, vertexAttrName, value, valueType):
        
        if not self.programID:
            raise Exception("Shader program not created. Call __init__() first.")
        
        location = glGetUniformLocation(self.programID, vertexAttrName)
       
        if location == -1:
            raise Exception(f"Uniform '{vertexAttrName}' not found in shader program.")
        if valueType == 'float':
            glUniform1f(location, value)
        elif valueType == 'int':
            glUniform1i(location, value)
        elif valueType == 'vec2':
            glUniform2f(location, *value)
        elif valueType == 'vec3':
            glUniform3f(location, *value)
        elif valueType == 'vec4':
            glUniform4f(location, *value)
        elif valueType == 'mat4':
            glUniformMatrix4fv(location, 1, GL_FALSE, value_ptr(value))
        
    def use(self):
        glUseProgram(self.programID)
        
    def deactivate(self):
        glUseProgram(0)  