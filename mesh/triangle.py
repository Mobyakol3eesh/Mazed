from OpenGL.GL import *
from core.opengl_buffers import openGLBuffer
from core.opengl_utilities import OpenGLUtilities
from mesh.shader import Shader

vertices = [
    -0.5,  -0.5, 0.0,  0.0, 1, 0.0,
     
    0.0, 0.5, 0.0,      1,0.0, 0.0,
    
    
    0.5, -0.5, 0.0,      0.0, 0.0, 1.0,
    
   
        ]

indices = [
    0,1,2,
    
]


class Triangle():
    def __init__(self, vertexShaderPath=r'\shader\triangle_shaderv.glsl', fragmentShaderPath=r"\shader\triangle_shaderf.glsl", vertices=vertices, indices=indices):
        self.vertices = vertices
        self.indices = indices
        self.shader = Shader(vertexShaderPath,fragmentShaderPath)
        
        
        
        self.glBuffer = openGLBuffer(vectorSize=3,stride=6)
        self.glBuffer.createVertexBuffRGB(self.vertices,vertexAttrIndex=0)
        self.glBuffer.createIndexBuffer(self.indices,vertexAttrIndex=0)
    
        
        

        
        




