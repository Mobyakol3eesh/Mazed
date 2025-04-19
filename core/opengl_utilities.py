from OpenGL.GL import *


class OpenGLUtilities:
    
    @staticmethod
    def createShader(shaderType, shaderSource):
        shaderID = glCreateShader(shaderType) 
        
        if shaderID == 0:
            raise RuntimeError("Failed to create shader")
        
        shaderSource =  "#version 330 core\n" + shaderSource 
        glShaderSource(shaderID, shaderSource)
        glCompileShader(shaderID)
        isSucced = glGetShaderiv(shaderID, GL_COMPILE_STATUS)
        if not isSucced:
            infoLog = glGetShaderInfoLog(shaderID).decode('utf-8')
            glDeleteShader(shaderID)
            raise RuntimeError(f"Shader compilation failed: {infoLog}")
        return shaderID
    @staticmethod
    def create_program(vertexshaderID, fragmentShaderID):
        program = glCreateProgram()
        if program == 0:
            raise RuntimeError("Failed to create program")
        
        glAttachShader(program, vertexshaderID)
        glAttachShader(program, fragmentShaderID)
        glLinkProgram(program)
        
        isSucced = glGetProgramiv(program, GL_LINK_STATUS)
        if not isSucced:
            infoLog = glGetProgramInfoLog(program).decode('utf-8')
            raise RuntimeError(f"Program linking failed: {infoLog}")
        glDeleteShader(vertexshaderID)
        glDeleteShader(fragmentShaderID)
        return program
        
        

    